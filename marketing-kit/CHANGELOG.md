# Changelog

## 2.0.0 (2026-10-22)

Rebuilt the plugin around a skill library and a manifest.

Added
- 73 new skills across ten categories (79 total); see CATALOG.md.
- Standardized skill manifest (`metadata` block) with JSON schema, generated registry (`registry/skills.json`), generated catalog and capability map.
- Shared references: MCP contract, model guide, node kinds, prompt grammar, platform specs, quality bar, brief and brand kit schemas.
- Motion design category with five vendored engines (cinetic, motionmaxxing, video-shotcraft, charlie-motion, howseen) and a hybrid Sloosh + code workflow.
- Validator, registry builder, capability map builder, packaging script, CI workflow, 154 eval scenarios.
- Docs: architecture, gap analysis, roadmap, testing, contributing, motion engine audit.

Changed
- `product-imagery`, `ad-variants` (now `static-ad-variants`), `product-video`, `published-spaces`, `ugc-storyboard` upgraded to 2.0.0 with model tables, QA steps, chains and examples.
- `launch-film` kept intact and wrapped in the manifest.

Verified against the live MCP on 2026-10-22: 44 tools, 23 image models, 17 video models, 52 node kinds, 18 templates, 112 catalogued Spaces.

## 1.1.0

Six skills: product-imagery, ad-variants, product-video, published-spaces, ugc-storyboard, launch-film.
