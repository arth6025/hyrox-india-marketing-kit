# Contributing

## Adding a skill

1. Copy `skills/product-imagery/` as a shape reference. Create `skills/<id>/SKILL.md`. Follow `docs/SKILL-AUTHORING.md`.
2. Only name tools, models, node kinds and Spaces that exist in `registry/*.json`. If you verified a new Space or model against the live server, add it to the registry with today's date first.
3. Set `status` honestly. `ready` is earned by a verified tool path, not by plausibility.
4. Add two scenarios to `evals/scenarios.json`.
5. Run `python3 scripts/validate_skills.py --evals`, then `python3 scripts/build_registry.py` and `python3 scripts/build_capability_map.py`. Commit the generated files too.
6. Open a PR with: what the skill makes, the tool path you ran, what you could not verify.

## Changing a skill

- Bump `metadata.version` (patch for wording, minor for new inputs or steps, major for changed inputs/outputs).
- If the change moves a chain, update both sides (`chains_to` here, `chains_from` there).
- Keep the body under 12 KB; move frameworks into `skills/<id>/references/`.

## Retiring a skill

Set `status: deprecated`, add `superseded_by`, keep the folder for one minor release, then delete it and the scenarios.

## Adding a motion engine

Vendor it under `engines/<name>/` with its LICENSE; rename its `SKILL.md` to `ENGINE.md` so hosts do not load it as a skill; add a row to `docs/MOTION-ENGINES.md` and `THIRD-PARTY-NOTICES.md`; reference exact file paths from `motion-film-code` or `motion-effects-library`.

## Style

Short sentences. Imperative. Say what Sloosh can and cannot do. No hype words, no em dashes, no "not X, it's Y" constructions in copy guidance. Quote credits in plain words. Never promise quality the skill cannot check; say what was checked.

## Review checklist

- [ ] Validator passes with zero errors
- [ ] Every paid step has quote → credits shown → approval → stable key
- [ ] `show_generation` once per request; videos and images apart; Space runs alone
- [ ] `view_asset` QA step with specifics
- [ ] Three examples that would route to this skill and not a sibling
- [ ] Status and `verified_on` truthful
- [ ] Generated registry, catalog and capability map committed
