# Roadmap

Three horizons. Each item names what ships, who owns it and the gap it closes (numbers from `docs/GAP-ANALYSIS.md`).

## Now (plugin 2.0, this package)

```
week 0 ─ install 2.0 internally ─ run evals/scenarios.json by hand on 20 scenarios
week 1 ─ validate the 5 needs-validation skills end to end ─ promote or demote
week 2 ─ pin the 60 Spaces the skills depend on (own copies or curated flag) ─ gap 15
week 3 ─ publish 2.1 to the team; collect verdicts per skill in evals/verdicts.md
```

- Run `scripts/validate_skills.py --evals` in CI on every PR (`.github/workflows/validate.yml`).
- Refresh `registry/capabilities.json` and `registry/spaces.json` from the live server before each release (`docs/TESTING.md`).
- Promote `needs-validation` skills after one observed end-to-end run each: `transitions-and-morphs`, `kinetic-typography`, `space-builder`, `batch-pipeline`, `shopify-store-audit`.

## Next (2.x, needs small MCP changes)

| Item | Closes | Unlocks |
|---|---|---|
| `upload_asset` (base64 / signed URL) | gap 1 | Claude Code and Cowork send local photos and rendered frames without the card |
| Fan-out in drafts under a cap | gap 4 | `batch-pipeline` and `space-builder` testable without an admin |
| `read_url` tool | gap 6 | `brand-kit-extract`, `shopify-store-audit`, `competitor-creative-teardown` become `ready` everywhere |
| `output_size` + white fill on bg-remove | gap 8 | `white-background-compliance`, `social-profile-kit`, `collection-banner` deliver exact specs |
| `enhance_prompt` edit modes | gap 16 | visible rewrites in `video-extend-edit` |
| Skill telemetry tags | gap 17 | usage and failure tracking per skill |
| 10 more Space-backed skills from unused Spaces | | `sketch-to-product-render`, `jewellery-on-model`, `room-restyle`, `poster-redesign`, `character-sheet` etc. (see CAPABILITY-MAP "Unused today") |

## Later (3.0, bigger MCP and product work)

| Item | Closes | Unlocks |
|---|---|---|
| `quote_generation` modes for audio and video post (TTS, music, subtitle, merge, trim, concat, deliver presets) | gaps 2, 3, 10, 12 | one-call reels, voiced clips, joined films; `cinematic-product-film` delivers one MP4; `reel-export` no longer needs ffmpeg |
| Text overlay and SVG logo overlay nodes | gap 7 | `kinetic-typography` and `logo-animation` become `ready` without a local engine |
| OCR + reference-similarity scores on outputs | gap 14 | automatic QA at batch scale; `brand-consistency-check` becomes measurable |
| Native skill runner in Sloosh Studio / Ask AI | native reuse | the same 79 skills inside the product; user-made skills from published Spaces |
| Hosted render for the motion engines (Remotion/HyperFrames in a Sloosh worker) | host gap | `motion-film-code`, `launch-film`, `ui-product-demo`, `animated-chart` run from the Claude app |
| Workspace voice library and longer TTS | gap 13 | brand voiceovers |

## Skill backlog (ordered by expected use)

1. `pdp-gallery-pack` (angles + lifestyle + macro + infographic, Shopify-sized) built on `product-multi-angle` + `amazon-listing-pack`.
2. `jewellery-on-model`, `sketch-to-product-render`, `room-restyle` (Spaces exist, unused).
3. `whatsapp-catalogue-cards` (square product cards with price and name).
4. `ad-localization` (same creative, five languages; text variants per language from one clean plate).
5. `creator-brief-kit` (shot list + reference frames for a human UGC creator).
6. `brand-mascot-system` (character-turnaround-sheet + mascot-pose-pack + consistent scenes).
7. `storyboard-animatic` (Space storyboard-to-animatic) folded into `motion-director` output.
8. `multi-sku-batch` wrapper over `batch-pipeline` with a CSV of SKUs (`output_filename` with `{{skuCode}}`).
9. `hosted-motion-render` once a render worker exists.
10. `skill-from-space` (wrap any published Space as a skill folder automatically).

## Maintenance cadence

- Weekly: `list_spaces` diff → update `registry/spaces.json`; `list_models` diff → `capabilities.json`; re-run validator.
- Per release: bump plugin version, regenerate catalog and capability map, package, upload.
- Quarterly: review `evals/verdicts.md`, demote skills with repeated failures, retire deprecated folders.
