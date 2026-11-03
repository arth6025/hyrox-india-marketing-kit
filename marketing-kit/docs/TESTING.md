# Testing

Three layers: static validation (seconds, CI), scenario evals (a person or an agent in a fresh session), and live capability refresh (before each release).

## 1. Static validation

```bash
pip install pyyaml jsonschema
python3 scripts/validate_skills.py --evals        # exit 1 on any error
python3 scripts/validate_skills.py --strict       # warnings fail too
python3 scripts/build_registry.py                 # regenerates registry/skills.json and CATALOG.md
python3 scripts/build_capability_map.py           # regenerates docs/CAPABILITY-MAP.md
```

What it checks per skill: frontmatter against `registry/manifest.schema.json`; folder name = `name`; every `mcp_tools` entry is a real tool; every model id and node kind is in `capabilities.json`; every Space id/slug pair is in `spaces.json`; every `chains_to/from/superseded_by` points at an existing skill; required sections exist; a skill that calls `generate`/`run_space`/`run_draft` mentions a quote; `ready` skills carry `verified_on`; deprecated skills carry `superseded_by`; body size warning above 12 KB; `{{tokens}}` outside canvas context warning. With `--evals`, every scenario names an existing skill and real tools.

CI: `.github/workflows/validate.yml` runs the same on every push and PR.

## 2. Scenario evals

`evals/scenarios.json` holds 154 scenarios, two per skill:

```json
{
  "id": "static-ad-variants-01",
  "skill": "static-ad-variants",
  "user_prompt": "Create three 9:16 ad variants for my summer sale on this sneaker",
  "expected_skill": "static-ad-variants",
  "expected_tools": ["get_connection", "list_models", "quote_generation"],
  "stop_condition": "waits for approval before generate",
  "pass": "...", "fail": "..."
}
```

Run them in a fresh session with the plugin installed and Sloosh connected (a human, or an agent acting as the user). Score each:

- **Routing**: the expected skill was chosen (or the router named it).
- **Order**: tools were called in the expected order up to the quote; no paid call before a quote; `get_connection` once.
- **Stop**: the session stopped at the stop condition and showed credits in plain words.
- **Honesty**: no invented model, Space or parameter; a missing capability was named.
- **Output**: for skills that generate, `view_asset` QA was reported with specifics.

Record verdicts in `evals/verdicts.md` as `date · scenario id · pass/partial/fail · one line`. Promote `needs-validation` skills to `ready` after one clean end-to-end run; demote any skill with two fails on the same step.

A cheap routing-only pass: paste ten `user_prompt`s and check which skill Claude names, without approving any quote. Nothing is spent.

## 3. Live capability refresh (before each release)

The server changes; the registry must follow.

1. `list_models` (no args) → compare ids, aspect ratios, constraints with `registry/capabilities.json`; update `models`, bump `verified_on`.
2. `list_node_kinds` short list, then `kinds` for the ten used in canvases → update `node_kinds`.
3. `list_spaces(scope: all, pageSize: 50)` pages 1–4 → diff slugs and ids with `registry/spaces.json`; remove vanished Spaces and check which skills listed them (`docs/CAPABILITY-MAP.md`); demote those skills or switch their primary route.
4. `get_guide` for each of the nine guides → diff against `references/mcp-contract.md`.
5. Re-run the validator; regenerate registry, catalog and capability map; bump the plugin version; `bash scripts/package.sh`.

The refresh is manual today. A `scripts/refresh_capabilities.py` that takes the raw JSON of the three list calls (saved from a session) and rewrites the registry is the first automation to add.

## 4. Install test

1. `bash scripts/package.sh` → `dist/sloosh-skills-<version>.zip`.
2. Claude app → Customize → Plugins → Add → Upload plugin → the zip. Connectors tab → Connect Sloosh → authorize the workspace.
3. In a new chat: "What can Sloosh do with this product photo?" → the router answers without spending.
4. "Make a studio photo of my water bottle on white" → upload card → model choice → quote with credits → approval → card → QA line.
5. In Claude Code: `/sloosh:motion-director` with a brand URL → MOTION brief; then `/sloosh:motion-film-code` → requirements check names Node, ffmpeg, Chromium.

## 5. Quality bar spot checks

Monthly, pick five generated outputs per top-tier skill and score them against `references/quality-bar.md` (fidelity, text, anatomy, composition, brand). Keep the sheet next to `evals/verdicts.md`. Prompt templates that fail twice get rewritten and the skill's `version` bumped.
