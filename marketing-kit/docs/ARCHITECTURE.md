# Sloosh plugin architecture

How 79 skills, one MCP server and five motion engines fit together, and why adding skill number 80 touches nothing but its own folder.

## The shape

```
                         user: "make our launch look good"
                                      │
                                      ▼
                     ┌─────────────────────────────────┐
                     │  Claude (any host)               │
                     │  loads name+description of every │  ← progressive disclosure:
                     │  skill at start (~79 × 1 line)   │    ~10 KB total, bodies on demand
                     └──────────────┬──────────────────┘
                                    │ picks
               ┌────────────────────┼────────────────────────┐
               ▼                    ▼                        ▼
      skills/sloosh-router   skills/<one skill>     skills/campaign-orchestrator
      (intent → skill/chain)  (SKILL.md body +       (rounds, approvals, budget)
                              references on demand)
                                    │
                                    │ calls, in the contract order
                                    ▼
      ┌─────────────────────────────────────────────────────────────────┐
      │  Sloosh MCP  https://mcp.sloosh.ai/mcp   (44 tools, 5 groups)   │
      │  account │ assets │ generation │ Spaces │ canvas authoring       │
      │  quote → approve → execute(idempotency key) → card → QA         │
      └───────┬───────────────┬────────────────────┬─────────────────────┘
              │               │                    │
              ▼               ▼                    ▼
       23 image models   112 catalogued      52 node kinds → your own
       17 video models   published Spaces     Spaces (TTS, music, lipsync,
       (list_models)     (list_spaces)        subtitles, concat, LLM, batch)

      ┌─────────────────────────────────────────────────────────────────┐
      │  engines/  (local, needs Claude Code or Cowork with a shell)    │
      │  cinetic · motionmaxxing · shotcraft · charlie-motion · howseen │
      │  code-rendered motion; Sloosh supplies plates, clips, audio     │
      └─────────────────────────────────────────────────────────────────┘
```

## Directory layout

```
sloosh-skills/
├── .claude-plugin/plugin.json     plugin identity and version (2.0.0)
├── .mcp.json                      the Sloosh MCP server (unchanged from 1.1.0)
├── skills/<id>/SKILL.md           79 skills, one folder each (+ references/, evals)
├── references/                    shared, read on demand by skills
│   ├── mcp-contract.md            the verified tool contract and call orders
│   ├── model-guide.md             model selection by role
│   ├── node-kinds.md              canvas nodes and recurring patterns
│   ├── prompt-grammar.md          image / video / edit prompt skeletons
│   ├── platform-specs.md          ratios, lengths, safe zones, compliance
│   ├── quality-bar.md             QA with view_asset, delivery standard
│   ├── brief-schema.md            the shared brief and handoff objects
│   └── brand-kit-schema.md        the brand kit object
├── registry/
│   ├── manifest.schema.json       JSON schema for skill frontmatter
│   ├── capabilities.json          verified tools, models, node kinds (generated from the live server)
│   ├── spaces.json                verified published Spaces by id
│   └── skills.json                GENERATED index of all skills (router + native surfaces read this)
├── engines/                       vendored motion engines (MIT / Apache-2.0), SKILL.md → ENGINE.md
├── workflows/                     multi-skill recipes (launch, new SKU, paid social, motion hybrid)
├── canvases/                      canvas blueprints (operation lists) for space-builder
├── evals/scenarios.json           154 routing/behaviour scenarios
├── scripts/                       validate_skills.py · build_registry.py · build_capability_map.py · package.sh
├── docs/                          this file, GAP-ANALYSIS, ROADMAP, TESTING, CONTRIBUTING, MOTION-ENGINES, CAPABILITY-MAP, SKILL-AUTHORING
├── CATALOG.md                     GENERATED human catalog
└── README.md · INSTALL.md · CHANGELOG.md · LICENSE · THIRD-PARTY-NOTICES.md
```

## Why this is extensible without touching the core

The plugin has no code path of its own. "Core" is four things that almost never change: the MCP server URL, the manifest schema, the shared references, and the two scripts that generate the registry and catalog. A new skill is a folder. The validator refuses it if it names a tool, model or Space that the live server did not list, or if it skips a required section. The registry builder picks it up. The router reads the registry. Nothing else knows the skill exists.

```
   add skills/<new>/SKILL.md
        │
        ▼
   python3 scripts/validate_skills.py     ← schema + capability + chain checks
        │ ok
        ▼
   python3 scripts/build_registry.py      ← registry/skills.json + CATALOG.md
        │
        ▼
   python3 scripts/build_capability_map.py
        │
        ▼
   bash scripts/package.sh                ← versioned zip for Claude upload
```

## The skill manifest (standardized)

Every `SKILL.md` carries the Agent Skills standard fields (`name`, `description`) plus a `metadata` block that is the Sloosh manifest: version, category, tier, status, cost, surfaces, `mcp_tools`, `spaces`, `models`, `node_kinds`, `inputs`, `outputs`, `chains_to/from`, `references`, `examples`, `adapted_from`. Hosts that do not know `metadata` ignore it; our tooling depends on it. Full schema: `registry/manifest.schema.json`; authoring guide: `docs/SKILL-AUTHORING.md`.

Status is the honesty field. `ready` means only verified tools. `ready-space` means the primary route is a public Space verified by id on `verified_on` and may vanish; each such skill carries a direct fallback route. `needs-validation`, `needs-local-agent` and `proposed` say exactly what is missing.

## Discovery and progressive disclosure

Three layers, each loaded only when needed:

1. **Descriptions** (always loaded): one paragraph per skill with trigger phrases. 79 × ~400 chars ≈ 30 KB worst case; the host truncates further.
2. **Skill body** (loaded when chosen): 4–10 KB of steps, prompts, QA.
3. **References** (loaded when the body says so): the contract, the model guide, platform specs, engine docs, shot indexes.

`sloosh-router` exists for requests that do not name an output; it reads `registry/skills.json` (not the bodies) and hands off. `campaign-orchestrator` runs chains in rounds with one approval per round and reads each step's handoff block (`references/brief-schema.md`).

## Execution contract

Every paid action follows one sequence, enforced by the skills and checked by the validator (a skill that calls `generate`/`run_space`/`run_draft` must mention a quote):

```
get_connection ─► discover (list_models | list_spaces+schema | list_node_kinds)
   ─► quote_* ─► show credits (+warning, budget) ─► USER APPROVES
   ─► generate | run_space | run_draft (idempotencyKey from the deliverable name, confirmed=true)
   ─► show_generation once ─► view_asset QA ─► handoff block
```

Idempotency keys double as asset names and test names (`brand-product-placement-concept-vN`), so a generation, its file and its ad-set variant share one identifier across Sloosh, the test plan and the user's ad account.

## Three execution routes per capability

Most skills document all three and say when each wins:

| Route | When | Cost shape | Needs |
|---|---|---|---|
| Direct generation (`quote_generation`) | one to four outputs, full control of model and prompt | per image / per clip | nothing |
| Published Space (`quote_space`) | a proven multi-step recipe exists (UGC ad, 360 orbit, try-on, captions) | capped hold, may include LLM tokens | the Space to still exist |
| Own canvas (`create_draft` … `publish`) | audio, subtitles, concat, LLM, batch over many SKUs, checkpoints | tokens + per node | `spacelab:author`; admin to publish; no fan-out in drafts |

Code-rendered motion is a fourth route that leaves the MCP: `engines/` on the user's computer, with Sloosh feeding plates, clips, music and upscales in and taking renders back through `import_asset`.

## Orchestration

```
brief-intake ──► brand-kit-extract ──► creative-strategy
      │                                      │
      ▼                                      ▼
product-imagery ──► static-ad-variants ──► creative-testing-plan
      │        └──► image-to-video ──► captions-subtitles ──► reels-shorts-clip
      │        └──► platform-content-pack
      └──► motion-director ──► motion-plates ──► motion-film-code ──► soundtrack-and-voice ──► reel-export
```

Chains are declared in each manifest (`chains_to`), validated to exist, printed in `CATALOG.md`, and used by the router and orchestrator. A handoff is a small YAML block with generated asset ids; the next skill resolves them with `get_asset` (never a card URL).

## Reuse across surfaces

| Surface | How skills run | What is missing |
|---|---|---|
| Claude app (plugin) | SKILL.md + MCP connector | local file by path (upload card instead); no shell (no code-rendered motion) |
| Claude Code / Cowork | same skills + shell | nothing; all 79 run |
| Sloosh MCP alone (no plugin) | tools only | the skills; users get raw tools |
| Sloosh native (Studio / Ask AI) | not yet | a skill runner that loads `registry/skills.json` and the chosen SKILL.md into the product's agent; see GAP-ANALYSIS |

The registry is JSON precisely so a native runner can load it without parsing Markdown. Skills never embed credentials; auth is the user's OAuth grant to the MCP, scoped per workspace (`spacelab:read/author/execute`), with a human-set daily ceiling and confirmation threshold that no skill can change.

## Versioning

- Skill: `metadata.version` semver, bumped per change; `status: deprecated` + `superseded_by` for one minor release before removal.
- Plugin: `.claude-plugin/plugin.json` minor per skill batch, major per schema change. `CHANGELOG.md` lists both.
- Capabilities: `registry/capabilities.json` and `registry/spaces.json` carry `verified_on`; refresh them from the live server before each release (`docs/TESTING.md`).
