# Sloosh skills

79 skills that turn Sloosh into a creative team you talk to: product imagery, performance ads, UGC and cinematic video, motion design, brand kits, social packs, catalogue sets, strategy and your own Spaces. Every skill quotes credits first and waits for your yes.

```
 you ──► "launch kit for the new sneaker" ──► router ──► brief ──► rounds
                                                                 │
   ┌─────────────────────────────────────────────────────────────┘
   ▼
 hero stills ─► ad variants ─► clips ─► motion piece ─► captions ─► test plan
 (approve)      (approve)      (approve)  (approve)      (approve)
```

## What is in the box

| Category | Skills | Examples |
|---|---|---|
| Orchestration | 5 | `sloosh-router`, `brief-intake`, `campaign-orchestrator`, `creative-iteration` |
| Image | 9 | `product-imagery`, `product-multi-angle`, `background-swap-relight`, `style-reference-transfer` |
| Advertising | 10 | `ad-concepts`, `static-ad-variants`, `ad-hook-matrix`, `testimonial-ads`, `creative-testing-plan` |
| AI video | 11 | `product-video`, `image-to-video`, `cinematic-product-film`, `ugc-video-ad`, `talking-head-video` |
| Motion design | 14 | `motion-director`, `motion-film-code`, `motion-effects-library`, `logo-animation`, `product-animation`, `launch-film` |
| Brand | 7 | `brand-kit-extract`, `logo-from-brief`, `brand-board`, `brand-consistency-check` |
| Social | 6 | `platform-content-pack`, `carousel-builder`, `youtube-thumbnail`, `reels-shorts-clip` |
| E-commerce | 8 | `amazon-listing-pack`, `ghost-mannequin`, `virtual-try-on`, `fashion-lookbook-set` |
| Strategy | 5 | `creative-strategy`, `shopify-store-audit`, `competitor-creative-teardown` |
| Authoring | 4 | `published-spaces`, `space-builder`, `batch-pipeline`, `prompt-enhancer-workflow` |

Full list with status, cost and example prompts: [CATALOG.md](CATALOG.md). Status today: 27 ready, 42 ready on a public Space, 5 need validation, 5 need a local agent.

## How it works

Skills are Markdown. The plugin has no code of its own. Claude reads one line per skill at start, loads a skill's body when it is chosen, and calls the Sloosh MCP (`https://mcp.sloosh.ai/mcp`, 44 tools) in one fixed order: discover → quote → show credits → you approve → execute with a stable key → result card → QA with `view_asset`.

Motion design is a first-class category: `motion-director` writes the beat map, Sloosh makes plates, clips, music and voice, and five vendored engines (`engines/`: cinetic, motionmaxxing, video-shotcraft, charlie-motion, howseen) render code-driven films in Claude Code or Cowork. See [docs/MOTION-ENGINES.md](docs/MOTION-ENGINES.md) and [workflows/motion-hybrid.md](workflows/motion-hybrid.md).

## Install

See [INSTALL.md](INSTALL.md). Short version: upload the zip as a plugin in Claude, connect Sloosh, set your daily allowance at https://sloosh.ai/settings/mcp.

## Spending

Sloosh blocks paid calls above your "Ask before spending more than" amount until you approve. Skills cannot raise your allowance, buy credits or change your plan. Default ceiling is 50 credits/day until you set one.

## Try saying

- "What can Sloosh do with this product photo?"
- "Three 4:5 ad variants for the serum, hook: wakes up a tired scalp"
- "Animate this packshot into a 5 second loop for the product page"
- "UGC ad for the face serum with this creator photo, 15 seconds, Hindi"
- "Logo reveal for our mark, 5 seconds, dark background"
- "Write the motion brief for our launch film, then make the plates"
- "Amazon listing pack for the bottle"
- "Is this creative on-brand?"
- "Build me a Space that turns one product photo into three scene images and a PDF"

## Extend

Add a folder under `skills/`, run `python3 scripts/validate_skills.py`, then `python3 scripts/build_registry.py`. Nothing else changes. Details: [docs/SKILL-AUTHORING.md](docs/SKILL-AUTHORING.md), [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).

## Documentation

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md): layout, manifest, discovery, execution contract, surfaces
- [docs/CAPABILITY-MAP.md](docs/CAPABILITY-MAP.md): every tool, model, node and Space → the skills that use it
- [docs/GAP-ANALYSIS.md](docs/GAP-ANALYSIS.md): what the MCP cannot do yet and what to change
- [docs/ROADMAP.md](docs/ROADMAP.md): now / next / later
- [docs/TESTING.md](docs/TESTING.md): validator, scenario evals, capability refresh
- [references/](references/): the MCP contract, model guide, node kinds, prompt grammar, platform specs, quality bar, brief and brand kit schemas

## Licenses

Plugin: MIT. Vendored engines keep their own licenses (MIT, Apache-2.0); see [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md). Marketing frameworks adapted from Corey Haines' marketing-skills (MIT) and Higgsfield's skills (MIT) are credited per skill in `adapted_from`.

## Support

- Documentation: https://sloosh.ai/docs/mcp
- Support: https://sloosh.ai/docs/support
- Privacy policy: https://sloosh.ai/privacy-policy
- Terms of use: https://sloosh.ai/terms-of-use
