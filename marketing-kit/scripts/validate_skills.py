#!/usr/bin/env python3
"""Validate every skills/<id>/SKILL.md against the manifest schema and the verified capability registry.

Usage: python3 scripts/validate_skills.py [--evals] [--strict]
Exit 1 on any error. Warnings do not fail unless --strict.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REG = ROOT / "registry"

try:
    import yaml  # type: ignore
except ImportError:  # minimal fallback: the frontmatter we write is simple YAML
    yaml = None

REQUIRED_SECTIONS = [
    "## When to use",
    "## Inputs",
    "## Tools",
    "## Steps",
    "## Outputs",
    "## Errors",
    "## Examples",
    "## Spending rules",
    "## Content from the workspace",
]


def load_frontmatter(text: str):
    m = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not m:
        raise ValueError("missing YAML frontmatter")
    if yaml is None:
        raise RuntimeError("PyYAML is required: pip install pyyaml")
    fm = yaml.safe_load(m.group(1))
    return _normalize(fm), text[m.end():]


def _normalize(obj):
    """YAML turns 2026-10-22 into a date and 1:1 into 61; keep dates as ISO strings and leave the rest."""
    import datetime as _dt
    if isinstance(obj, dict):
        return {k: _normalize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_normalize(v) for v in obj]
    if isinstance(obj, (_dt.date, _dt.datetime)):
        return obj.isoformat()
    return obj


def main(argv):
    strict = "--strict" in argv
    check_evals = "--evals" in argv
    errors, warnings = [], []

    cap = json.loads((REG / "capabilities.json").read_text())
    spaces = json.loads((REG / "spaces.json").read_text())
    tools = set(cap["tools"])
    image_models = {m["id"] for m in cap["models"]["image"]["list"]}
    video_models = {m["id"] for m in cap["models"]["video"]["list"]}
    node_kinds = set(cap["node_kinds"].keys())
    space_ids = {s["spaceId"]: s for s in spaces["spaces"]}
    space_slugs = {s["slug"]: s for s in spaces["spaces"]}

    try:
        import jsonschema  # type: ignore
        schema = json.loads((REG / "manifest.schema.json").read_text())
        validator = jsonschema.Draft202012Validator(schema)
    except ImportError:
        validator = None
        warnings.append("jsonschema not installed; schema validation skipped (pip install jsonschema)")

    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir() and not p.name.startswith("_"))
    names = set()
    manifests = {}
    for d in skill_dirs:
        f = d / "SKILL.md"
        tag = f"skills/{d.name}"
        if not f.exists():
            errors.append(f"{tag}: SKILL.md missing")
            continue
        text = f.read_text(encoding="utf-8")
        try:
            fm, body = load_frontmatter(text)
        except Exception as e:  # noqa
            errors.append(f"{tag}: {e}")
            continue
        if fm.get("name") != d.name:
            errors.append(f"{tag}: name '{fm.get('name')}' != folder")
        names.add(d.name)
        manifests[d.name] = fm
        if validator:
            for err in sorted(validator.iter_errors(fm), key=lambda e: list(e.path)):
                errors.append(f"{tag}: schema: {'/'.join(str(p) for p in err.path)}: {err.message[:160]}")
        md = fm.get("metadata", {}) or {}
        for t in md.get("mcp_tools", []) or []:
            if t not in tools:
                errors.append(f"{tag}: unknown MCP tool '{t}'")
        for s in md.get("spaces", []) or []:
            sid, slug = s.get("spaceId"), s.get("slug")
            if sid not in space_ids:
                errors.append(f"{tag}: space id {sid} not in registry/spaces.json")
            elif slug and space_ids[sid]["slug"] != slug:
                errors.append(f"{tag}: space slug '{slug}' does not match id {sid} ({space_ids[sid]['slug']})")
        models = md.get("models", {}) or {}
        for mid in models.get("image", []) or []:
            if mid not in image_models:
                errors.append(f"{tag}: unknown image model '{mid}'")
        for mid in models.get("video", []) or []:
            if mid not in video_models and mid not in {"vidu-q4", "kling-3.0-motion-control-pro", "kling-3.0-motion-control-standard", "omnihuman-2"}:
                errors.append(f"{tag}: unknown video model '{mid}'")
        for k in md.get("node_kinds", []) or []:
            if k not in node_kinds:
                errors.append(f"{tag}: unknown node kind '{k}'")
        for ref in md.get("references", []) or []:
            if not (ROOT / ref).exists() and not (d / ref).exists():
                errors.append(f"{tag}: reference '{ref}' not found")
        # body checks
        if len(body.encode()) > 12000:
            warnings.append(f"{tag}: body is {len(body.encode())} bytes; consider moving detail to references")
        for sec in REQUIRED_SECTIONS:
            if sec.lower() not in body.lower():
                errors.append(f"{tag}: missing section '{sec}'")
        paid = {"generate", "run_space", "run_draft"} & set(md.get("mcp_tools", []) or [])
        if paid and "quote" not in body.lower():
            errors.append(f"{tag}: calls {sorted(paid)} but never mentions a quote")
        if "generate" in paid and "show_generation" not in (md.get("mcp_tools") or []):
            warnings.append(f"{tag}: calls generate without show_generation")
        if re.search(r"\{\{\w+\}\}", body) and "canvas" not in body.lower():
            warnings.append(f"{tag}: contains {{{{tokens}}}} outside a canvas context")
        if md.get("status") in ("ready", "ready-space") and not md.get("verified_on"):
            errors.append(f"{tag}: status {md.get('status')} needs verified_on")
        if md.get("status") == "deprecated" and not md.get("superseded_by"):
            errors.append(f"{tag}: deprecated without superseded_by")

    # cross-skill chain integrity
    for n, fm in manifests.items():
        md = fm.get("metadata", {}) or {}
        for key in ("chains_to", "chains_from", "superseded_by"):
            vals = md.get(key)
            if not vals:
                continue
            for v in (vals if isinstance(vals, list) else [vals]):
                if v not in names:
                    errors.append(f"skills/{n}: {key} -> unknown skill '{v}'")

    if check_evals:
        ev = ROOT / "evals" / "scenarios.json"
        if ev.exists():
            for sc in json.loads(ev.read_text()):
                if sc.get("expected_skill") not in names:
                    errors.append(f"evals: scenario '{sc.get('id')}' expects unknown skill {sc.get('expected_skill')}")
                for t in sc.get("expected_tools", []):
                    if t not in tools:
                        errors.append(f"evals: scenario '{sc.get('id')}' names unknown tool {t}")
        else:
            warnings.append("evals/scenarios.json missing")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(skill_dirs)} skills, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors or (strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
