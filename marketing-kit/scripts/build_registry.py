#!/usr/bin/env python3
"""Build registry/skills.json and CATALOG.md from every skills/<id>/SKILL.md frontmatter.

The registry is what the router skill reads (progressive disclosure: id, description, category,
tier, status, cost, examples, chains) and what native surfaces can load without parsing Markdown.
"""
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import yaml  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
OUT_JSON = ROOT / "registry" / "skills.json"
OUT_MD = ROOT / "CATALOG.md"

CATEGORY_ORDER = [
    ("orchestration", "Orchestration and intake"),
    ("image", "Image generation and editing"),
    ("advertising", "Performance advertising"),
    ("video", "AI video"),
    ("motion", "Motion design"),
    ("brand", "Brand identity"),
    ("social", "Social content"),
    ("ecommerce", "E-commerce and catalogue"),
    ("strategy", "Creative strategy and analysis"),
    ("authoring", "Canvas and Space authoring"),
]
STATUS_LABEL = {
    "ready": "Ready",
    "ready-space": "Ready (public Space)",
    "needs-validation": "Needs validation",
    "needs-local-agent": "Needs local agent",
    "proposed": "Proposed",
    "deprecated": "Deprecated",
}


def frontmatter(text):
    m = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    return _normalize(yaml.safe_load(m.group(1)))


def _normalize(obj):
    import datetime as _dt
    if isinstance(obj, dict):
        return {k: _normalize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_normalize(v) for v in obj]
    if isinstance(obj, (_dt.date, _dt.datetime)):
        return obj.isoformat()
    return obj


def main():
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    skills = []
    for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        f = d / "SKILL.md"
        if not f.exists():
            continue
        fm = frontmatter(f.read_text(encoding="utf-8"))
        md = fm.get("metadata", {}) or {}
        skills.append({
            "id": fm["name"],
            "path": f"skills/{d.name}/SKILL.md",
            "description": fm["description"],
            **{k: md.get(k) for k in (
                "version", "category", "subcategory", "tier", "status", "superseded_by", "verified_on", "cost",
                "surfaces", "mcp_tools", "spaces", "models", "node_kinds", "inputs", "outputs",
                "chains_to", "chains_from", "references", "examples", "adapted_from", "tags")},
        })
    registry = {
        "plugin": plugin["name"],
        "plugin_version": plugin["version"],
        "generated_on": date.today().isoformat(),
        "manifest_schema": "registry/manifest.schema.json",
        "count": len(skills),
        "by_status": dict(sorted(defaultdict(int, {s: sum(1 for k in skills if k["status"] == s) for s in STATUS_LABEL}).items())),
        "skills": skills,
    }
    OUT_JSON.write_text(json.dumps(registry, indent=1, ensure_ascii=False) + "\n")

    by_cat = defaultdict(list)
    for s in skills:
        by_cat[s["category"]].append(s)
    lines = [
        "# Sloosh skill catalog",
        "",
        f"{len(skills)} skills · plugin {plugin['version']} · generated {registry['generated_on']} by `scripts/build_registry.py`. "
        "Status legend: **Ready** = verified MCP tools only · **Ready (public Space)** = depends on a published Space verified by id · "
        "**Needs validation** = tool path exists, end-to-end run not yet observed · **Needs local agent** = runs in Claude Code or Cowork with a shell · "
        "**Proposed** = needs an MCP or product change (see docs/GAP-ANALYSIS.md).",
        "",
        "| Status | Count |", "|---|---|",
    ]
    for st, label in STATUS_LABEL.items():
        n = registry["by_status"].get(st, 0)
        if n:
            lines.append(f"| {label} | {n} |")
    lines.append("")
    for cat, title in CATEGORY_ORDER:
        items = sorted(by_cat.get(cat, []), key=lambda s: (s["tier"], s["id"]))
        if not items:
            continue
        lines += [f"## {title}", "", "| Skill | Tier | Status | Cost | What it makes | Try saying |", "|---|---|---|---|---|---|"]
        for s in items:
            desc = s["description"].split(". ")[0].rstrip(".")
            ex = (s.get("examples") or [""])[0]
            lines.append(f"| [`{s['id']}`]({s['path']}) | {s['tier']} | {STATUS_LABEL[s['status']]} | {s['cost']} | {desc} | “{ex}” |")
        lines.append("")
    # chains
    lines += ["## Common chains", "", "```"]
    seen = set()
    for s in skills:
        for t in s.get("chains_to") or []:
            key = (s["id"], t)
            if key not in seen:
                seen.add(key)
                lines.append(f"{s['id']:<32} → {t}")
    lines += ["```", ""]
    OUT_MD.write_text("\n".join(lines))
    print(f"wrote {OUT_JSON.relative_to(ROOT)} and {OUT_MD.relative_to(ROOT)}: {len(skills)} skills")


if __name__ == "__main__":
    sys.exit(main())
