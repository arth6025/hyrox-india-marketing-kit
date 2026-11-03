# Gap analysis

What works now, what the Sloosh MCP cannot do yet, and what each gap blocks. Verified against the live server on 2026-10-22; collected from the 79 skill authors' notes.

## Works today (no change needed)

- 27 skills run on verified MCP tools alone; 42 more run on public Spaces verified by id, each with a direct fallback.
- Direct image and video generation with quotes, approvals, idempotent retries, result cards and `view_asset` QA.
- Every published Space in the catalogue (112 indexed) via schema-driven inputs, capped holds and checkpoints.
- Canvas authoring end to end: templates, examples, node schemas, atomic edits, validation, draft runs, publish (admin).
- Free prompt enhancement, free colour grading, cheap draft models.

## Gaps in the MCP

| # | Gap | Blocks | Workaround today | Proposed change | Effort |
|---|---|---|---|---|---|
| 1 | No local file upload by path (only the upload card or public https `import_asset`) | Claude Code / Cowork handing rendered frames or local product photos to Sloosh without a public URL | user uploads in the card; or host serves a temporary https URL | `upload_asset` tool accepting base64 or a signed upload URL flow | S |
| 2 | No audio through `quote_generation` (music, TTS, lipsync, subtitles, mux are canvas/Space only) | one-call reels, voiced clips, captioned ads | run `add-captions`, `add-a-soundtrack`, `talking-clip` Spaces, or a built canvas | `mode: audio_gen` (Lyria/TTS) and `mode: video_post` (subtitle, merge, trim) on `quote_generation` | M |
| 3 | No concat / trim / frame extract outside a canvas | multi-shot films as one MP4; using a video frame as the next start frame | `space-builder` with `video-concat`; or the user's editor | post-processing modes as in #2 | M |
| 4 | Draft runs refuse fan-out | testing a batch canvas before publishing; batches without an admin | publish first (admin), then run | allow fan-out in drafts under a sample cap (e.g. ≤ 4 items) | S |
| 5 | No LLM (`text-gen`) outside a canvas | reusing copy/planning skills from a native surface; Spaces that must write at run time already work | Claude writes copy in the host | optional `text` mode or a "text-only Space" template | S |
| 6 | No web page reader outside the `url-input` node | store audits, brand extraction without host browsing | host web access, screenshots, or a `url-input → text-gen` canvas (tokens) | `read_url` tool returning text + images, no credits | S |
| 7 | Rendered text is unreliable in AI video; no vector output anywhere | kinetic typography, logo stings with exact marks | code engines (local); stills from GPT Image 2.5 / Ideogram | expose a text-overlay node (Veed-style titles) and SVG logo overlay in `merge`/`subtitle` nodes | M |
| 8 | No exact pixel output; render by ratio and 1K/2K/4K | marketplace and banner specs (1584×396, 1200×628), strict RGB 255 white | `image-resize` node in a canvas; local resize | `output_size` on `quote_generation`; `background: "#FFFFFF"` flag on bg-remove | S |
| 9 | No seed on most video models; no determinism | re-rendering a near-miss clip identically | keep the good clip, edit with `video_edit` | surface seed where providers support it | S |
| 10 | No delivery controls (loudness, yuv420p/bt709 tagging, container, silent AAC track) | upload-clean Reels/TikTok files | `reel-export` (local ffmpeg) | a `deliver` post-processing node/mode with platform presets | M |
| 11 | No caption text correction | brand names mis-transcribed by `video-subtitle` / Add Captions | re-run with a hint, or local tools | accept an SRT/words JSON input on the subtitle node | S |
| 12 | No audio mixer (music + VO + SFX with ducking) | sound design in one pass | two merges, or local mix | `audio-mix` node with ducking and gains | M |
| 13 | TTS ≤ 1000 chars, stock voices only, no cloning | long voiceovers, brand voices | split scripts; ElevenLabs via motionmaxxing locally | raise cap; voice library per workspace | M |
| 14 | No per-output quality signal (fidelity score, OCR of rendered text) | automatic QA at batch scale | `view_asset` + Claude judgement; `enable_eval` on `image-gen` nodes only | return OCR text and a reference-similarity score with each image output | M |
| 15 | Public Spaces are owned by other workspaces and can change | 42 `ready-space` skills | registry `verified_on`; direct fallbacks | a "curated" or "pinned" Space flag with versioned `catalogVersion`, or ShopOS-owned copies of the 60 Spaces skills rely on | S |
| 16 | `enhance_prompt` has no video_edit / video_extend modes | visible rewrites for edits | write the edit prompt by hand | add the modes | S |
| 17 | No usage/feedback telemetry per skill | measuring which skills work, failure tracking | none (host-side only) | optional `skill` and `scenario` tags on `generate`/`run_space` for analytics | S |

## Gaps in the plugin host

| Gap | Effect | Mitigation |
|---|---|---|
| Claude app has no shell | 5 `needs-local-agent` skills (code-rendered motion, ffmpeg export, charts) only run in Claude Code / Cowork | skills say so and offer the Sloosh-only route |
| Description budget | 79 descriptions compete for the host's skill list | descriptions carry triggers in the first sentence; `sloosh-router` covers the long tail |
| Shared `references/` live outside skill folders | hosts that sync only `skills/` would miss them | package.sh includes them; if a host drops them, copy `references/` into `skills/_shared/` (validator accepts both paths) |

## Gaps for native reuse (Sloosh product)

- A skill runner: load `registry/skills.json`, pick by description, load `SKILL.md`, give the product's agent the same MCP tools. The registry is JSON for this reason.
- Permissions: skills assume the user's grant and ceiling; a native runner must apply the same daily limit and confirmation threshold.
- User-made skills: the manifest schema plus `space-builder` already let a user publish a Space and wrap it in a skill folder; a UI that writes the folder from a published Space is the missing piece.

## Things we did not verify and marked accordingly

- End-to-end runs of start/end-frame morphs (`transitions-and-morphs`, `kinetic-typography`, logo route C) and of multi-reference consistency claims: `needs-validation`.
- `image-resize` fill colour and `bg-remove` output on strict-white compliance: confirm with `list_node_kinds(kinds:["image-resize","bg-remove"])` before relying on it.
- Any Space's exact input field ids: always read `get_space_input_schema` at run time.
