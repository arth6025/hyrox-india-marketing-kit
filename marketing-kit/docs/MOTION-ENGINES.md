# Motion engines audit

Five motion design skill repositories were reviewed on 2026-10-22 and vendored under `engines/`. None of them talks to Sloosh today. All five render motion **from code** on the user's computer (HTML, GSAP or React drawn frame by frame in headless Chromium, encoded with ffmpeg). That is the opposite of AI video generation and it is why they matter: code gives exact type, exact UI and exact timing; Sloosh gives photoreal plates, product clips, music, voice and restyling. The motion skills in this plugin combine the two.

Each repo's own `SKILL.md` was renamed `ENGINE.md` so the plugin loader does not register it as a skill. The Sloosh skills point at the exact engine files to read at run time, so the engines stay upgradeable in place.

## Summary table

| Engine | What it is | Stack | Requires on the user's computer | Best for | What Sloosh adds | License | Vendored at | Not vendored |
|---|---|---|---|---|---|---|---|---|
| **cinetic** (Leonxlnx) | Film-grade direction and build system: beat-locked timeline drives picture and a synthesized score; hard bans; measured technique library; critique loop with scripts | Remotion 4 (default) or HyperFrames 0.8 (HTML + GSAP); Python QA scripts | Node 22+, ffmpeg 6+ (libx264), Python 3.11+ with numpy, scipy, soundfile, pyloudnorm, opencv-python, librosa (fonttools, brotli, uharfbuzz for outlined logos; pillow), Chromium or Chrome Headless Shell | Launch films, feature loops, logo stings, UI walkthroughs where sync, finishing (motion blur, BT.709, loudness) and taste discipline matter | Photoreal plates and hero surfaces (`motion-plates`), product clips as layers (`image-to-video`), music or voice when no synth score is wanted (`soundtrack-and-voice`), AI restyle of a render (`video_edit`), 4K lift (`video-upscale-master`) | MIT | `engines/cinetic/` (ENGINE.md, 19 references, 27 scripts, remotion-starter, hyperframes-starter) | nothing material |
| **motionmaxxing** (makwanatejas170) | Idea-first director: finds the idea only this brand can film, builds a world, animates with 12 eases measured from 53 pro films, and refuses to self-certify: `look.py` and `lint.mjs` compute gates G0–G5 | Plain HTML + seek-safe GSAP runtime (`runtime/motion.js`), optional three.js `hero3d`; Node render via CDP; Python look/mix | Node 22+, Chrome, ffmpeg, Python 3 (numpy, Pillow, opencv); ElevenLabs key for VO/SFX/music (optional); Codex image gen optional | Brand stings, kinetic type, promos that must not look generated; honest QA numbers; 3D hero text and logos | Hero surfaces and generated plates in place of Codex image gen (`motion-plates`), AI product clips, logo in material (`textured-logo`), voice and music through a Space or canvas when there is no ElevenLabs key | Apache-2.0 | `engines/motionmaxxing/` (ENGINE.md, 14 references, 13 scripts, runtime incl. three.js and GSAP, templates, taste, library) | `studies/` (1.1 MB of study JPGs), `docs/media` and `docs/hero` (README media), `examples/` |
| **video-shotcraft** (Vincentwei1021) | 124 shot recipe cards (150 shots) in 10 categories, a validated "Ink Press" promo template, 2.5D camera moves over real page screenshots, beat sync, sound design, JianYing export, browser workbench | Remotion (React), some cards use `@remotion/three`, `@remotion/motion-blur`; Chinese-language docs | Node, ffmpeg, Remotion deps per `template/package.json`; Python for demo smoke renders | Web and app product promos from real screenshots; picking a named shot ("flying-words", "spotlight-hero-card") for one moment | Ambient plates and textures behind UI, product stills for non-software products, music via `add-a-soundtrack`, talking segments via `multi-camera-edit` Space | Apache-2.0 | `engines/shotcraft/` (ENGINE.md, README, references incl. all 124 cards, template, assets) | `workbench/` (4.6 MB CapCut-style editor), `shot-polish/` (1.7 MB polish tooling), `videos/`, `publish/`, `jianying-export/`, `package-lock.json`; they are optional tooling and the heaviest files |
| **motion-graphics-skills** (Charlie Hills) | 15 small, opinionated formats: brand-intake, motion-brief-writer, motion-prompt-writer, motion-effects (16 recipes), animated-chart, milestone-reveal, loop-cover, reel-export, reference-to-motion, title-sequence-3d, vox-explainer, newsletter-promo, launch-video, apple-launch-film, model-showdown | One HTML file with `window.seek(seconds)`, exported through HyperFrames or Playwright + ffmpeg; Three.js for the title sequence | Claude Code (or Codex), Chromium, ffmpeg; HyperFrames via `npx skills add heygen-com/hyperframes` | Single-purpose social graphics with exact numbers (charts, milestones), loop covers, vertical export, turning references into prompts | Plates and covers (`motion-plates`), static infographic frames (`sensenova-u1-infographic`), reel safe-zone stills (`change-aspect-ratio`), music | MIT | `engines/charlie-motion/` (15 skill folders as ENGINE.md, prompts/, README, LICENSE) | `assets/readme/` images |
| **claude-motion-design** (Howseen, Raphaël Aubry) | A working studio's full code-only pipeline: brief → beat map → stills → `seek(t)` HTML engine → Playwright render → ffmpeg → Mixkit music and SFX → QA; a "remake this reference video" sub-pipeline; asset sourcing (Mixkit, Pexels, Unsplash, svgl logos, 21st.dev components) | Bare HTML, Python render and audio templates | Python 3 with Playwright, imageio-ffmpeg, numpy, librosa; yt-dlp for references; Firecrawl key optional | Fast, cheap, deterministic films; remaking a reference's rhythm; practical gotchas (Chromium flags, subframe blur, caption rules) | Replaces stock footage with generated product plates and clips; `video-analyzer` canvas node for reference breakdown; AI recreation of a reference through Spaces (`shadow-clone`, `custom-character-motion-video-replicator`) | MIT | `engines/howseen/` (ENGINE.md, 7 scripts incl. `remake/`, README, LICENSE) | `examples/howseen-launch/` (one finished film; personal paths and brand) |

Plus the existing **launch-film** skill (ShopOS, Sloosh plugin 1.1.0): Remotion, match cuts measured in pixels, whisper word timings, SFX cue sheets, 4K master. It stays as its own skill and is the Remotion route for voiceover-led films.

## Execution models, side by side

| Model | Engines | How a frame is made | Strength | Cost |
|---|---|---|---|---|
| Remotion (React, frame-driven) | cinetic, launch-film, shotcraft | `useCurrentFrame()` per component; `npx remotion render` | Component reuse, real UI rebuilt as React, motion blur package, transitions package | Node project, npm install, slower renders |
| HTML + paused GSAP (HyperFrames) | cinetic (alt), motionmaxxing, charlie (export) | GSAP timeline seeked to `t`, screenshot per frame | Fast authoring, designer-friendly, `--batch` variable renders | GSAP seek quirks (handled by runtimes) |
| Bare HTML `seek(t)` | howseen, charlie formats | Everything a pure function of time; Playwright screenshots; ffmpeg encodes with subframe blend | Deterministic, zero deps beyond Python + Chromium, parallel chunk renders | Hand-rolled springs and camera |
| AI video (Sloosh) | this plugin's `product-animation`, `transitions-and-morphs`, `logo-animation`, `image-to-video` | A model renders motion from a prompt and frames | Photoreal, physics, light; no code | Credits; text and logos can drift; no exact timing |

## What the engines share (and what the Sloosh skills keep)

- One idea, one device, one accent; copy budget ≤ 5 words per line.
- A beat grid (BPM) that every cut lands on; the drop on the key visual moment.
- Stills before motion: render 3–5 frames and look before a full render.
- Measured review: contact sheets, loop seam check, loudness, sync; never self-certify.
- Real UI only; never invent screens; label anything illustrative.
- Anti-slop bans: no eyebrow labels, no rainbow gradients, no particles for "AI", no bouncy overshoot, no page chrome.

These rules are now in `skills/motion-director` (the brief) and enforced in `skills/motion-film-code` (the build) and `skills/kinetic-typography`.

## Where Sloosh plugs in (verified tools only)

| Engine step | Sloosh capability | MCP tool / node / Space |
|---|---|---|
| Hero surface, background, texture, product cut-out | image generation + bg removal | `quote_generation` (image_gen), Space `background-remover-3`, canvas `bg-remove` / `auto-mask` |
| 3D-looking hero render, logo in material | image generation | Nano Banana Pro / GPT Image 2.5 at 4K; Space `textured-logo` |
| Footage layer (product turning, pouring, floating) | video generation | `quote_generation` (video_gen) with `start_frame`; Spaces in `product-animation` |
| Scene transition between two stills | start + end frame video | `kling-o3`, `kling-v3-omni-video`, `seedance-2.5` |
| Music bed | Lyria 3 | canvas `lyria-3`; Space `add-a-soundtrack` |
| Voiceover | ElevenLabs stock voices | canvas `text-to-speech` (≤ 1000 chars); Space `talking-clip` |
| Captions | Veed | canvas `video-subtitle`; Space `add-captions` |
| Restyle or relight a rendered film | video edit | `quote_generation` mode `video_edit` (`gemini-omni-1.1-flash`, `seedance-2.5`) |
| Sharper master | video upscale | Space `video-upscale`; canvas `video-upscale` |
| Reference breakdown | video analysis | canvas `video-analyzer` (Gemini) |
| Bring a render into Sloosh | import | `import_asset` from an https URL (the agent must host the file; no local path upload) |
| Take Sloosh output into the project | download | `get_asset` → `access.url` → download into `public/` |

## What the MCP cannot do for motion today (gaps)

1. No local file upload by path; a rendered MP4 reaches Sloosh only through the upload card or a public https URL.
2. No audio, captions, concat, trim, frame extraction or mux through `quote_generation`; all of these are canvas nodes or Spaces, so a code film needs a published Space (or a draft run without fan-out) to use them.
3. No vector or text rendering; AI video mutates glyphs and marks. Logos and copy stay in code.
4. No alpha or ProRes output; cut-outs are PNG stills only, clips are H.264.
5. No frame-exact timing control; durations snap to model ranges (4–30 s), cuts inside a clip are prompt-driven.
6. No reframe or re-encode of a finished video (the `reel-export` step stays local ffmpeg).
7. No seed on most video models, so a re-render is never identical; code renders are.

See `docs/GAP-ANALYSIS.md` for the proposed MCP additions.
