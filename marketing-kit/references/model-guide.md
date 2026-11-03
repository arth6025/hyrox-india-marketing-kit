# Model guide

Catalog read from `list_models` on 2026-10-22. Ids rotate; every skill calls `list_models` at run time and uses this file only to choose. If an id below is missing at run time, pick the nearest row by role.

## Image models (23)

Default: `gemini-nano-banana-2.1`.

| Role | First pick | Second | Why |
|---|---|---|---|
| Campaign hero, product photography, typography | `gemini-3-pro-image-preview` (Nano Banana Pro) | `gpt-image-2.5-sunburst` | Realism, text, 4K, 14 refs |
| Fast everyday product shots, iterative edits | `gemini-nano-banana-2.1` | `gemini-3.1-flash-image-preview` | Speed, consistency, 14 refs |
| Cheap drafts, bulk exploration, moodboards | `gemini-3.1-flash-lite-image` | `gemini-3.1-flash-image-preview` (512 option) | Lowest cost |
| Precise edits of an existing image, text on image, design layouts | `gpt-image-2.5-sunburst` | `gpt-image-2` | Edit precision, text rendering, 16 refs |
| Keep untouched pixels intact across repeated edits | `ideogram-4.5` | `gpt-image-2.5-sunburst` | Pixel-faithful edits at native res |
| Multi-reference composites (product + model + scene) | `seedream-5-0-pro` | `kling-image-o3`, `flux-2-pro` | 10 refs, region editing |
| Photoreal people and lifestyle | `krea-3` | `seedream-4.5` | Photoreal bias |
| Batch sets of one subject (up to 10 per call) | `muse-image-1.0` | `seedream-4.5` | `num_images` 1–10 on canvas |
| Infographics, comparison charts, data cards | `sensenova-u1-infographic` | `gpt-image-2.5-sunburst` | Laid-out charts and legible text |
| Brand/editorial layout, posters, icons | `recraft-v4.1-flash` (no refs) | `gpt-image-2.5-sunburst` | Design-first |
| Seeded reproducibility | `flux-2-pro`, `krea-3`, `seedream-*`, `qwen-image-3`, `ideogram-4.5` | | Expose `seed` |
| Ultrawide / tall (21:9, 9:21) | `krea-3`, `seedream-4.5`, `muse-image-1.0`, `qwen-image-3` | | Only these list 9:21 |

Limits worth remembering: `kling-image-3.0` and `qwen-image-2-pro` take 1 reference; `recraft-v4.1-flash` and `sensenova-u1-infographic` take none; `qwen-image-3` takes 3; `grok-imagine-image-2.0` and `ideogram-4.5` take 5. Max prompt chars: Gemini family 50 000; GPT family 32 000; most others 5 000; Kling 2 500.

Aspect ratios: `4:5` (feed) is missing on `grok-imagine-image-2.0`, `kling-image-3.0`, `kling-image-o3`, `muse-image-1.0`, `wan-2.7-image-pro`, `flux-3-image-klein`. For a 4:5 deliverable from those, generate 1:1 or 3:4 and reframe with the Change Aspect Ratio Space or an `image-resize` node.

## Video models (18)

Default: `seedance-2.5`.

| Role | First pick | Second | Notes |
|---|---|---|---|
| Product film, multi-reference, long takes (4–30 s) | `seedance-2.5` | `seedance-2.0` | 30 ref images, 10 ref videos, start/end frames, 1080p, audio |
| Fast / cheap clips | `seedance-2.0-fast` | `minimax-h3-max-turbo` | 720p, 4–15 s |
| Animate one still with a required start frame | `kling-3.0` | `kling-2.5` | Start frame required; 3.0 adds end frame, audio, multi-shot prompts |
| Start + end frame morph (pose to pose, before/after) | `kling-o3` | `kling-v3-omni-video`, `seedance-2.5` | Consistent characters, 3–15 s |
| 4K delivery | `kling-v3-omni-video`, `seedance-2.0`, `minimax-h3`, `gemini-omni-1.1-flash` | | |
| Lip-synced speech, native audio | `grok-imagine-1.5` (1080p) | `happy-horse-1.1` | Grok 1–15 s; Happy Horse 3–15 s, 9 refs |
| Reference-conditioned (character + motion video + audio) | `minimax-h3-reference` | `minimax-h3-max-reference`, `wan-3.0` | H3 ref mode: 9 images, 3 videos, 3 audio; cannot mix with start frame |
| Conversational edit of an existing clip | `gemini-omni-1.1-flash` | `seedance-2.5` (video_edit) | ≤ 10 s source, 3–10 s out |
| Ultrawide 21:9 | `minimax-h3*`, `seedance-*`, `happy-horse-1.1`, `grok-imagine-1.5` | | |
| Seed control | `happy-horse-1.1`, `minimax-h3*`, `wan-3.0` | | |

Durations: Seedance 2.5 4–30 s; Wan 3 only 5/10/15/30; MiniMax turbo only 5/10/15; Kling 2.5 only 5/10; Grok 1.5 4/6/8/10/15.

Canvas-only video models (not quotable through `quote_generation`): `vidu-q4`, `kling-3.0-motion-control-pro/standard` (character image + motion video), `omnihuman-2` (person + speech audio), video-edit ids `happy-horse-video-edit`, `kling-o3-edit`, `minimax-h3-max-recast`, `minimax-h3-max-relight`.

## Text models (canvas `text-gen` only)

Default `claude-sonnet-4-6`. The enum lists 18 ids; use only ones `list_models(category: "text")` marks `quotable`. Token-priced. Skills do their own writing in Claude; use `text-gen` inside a Space when the Space itself must write (scripts, copy, shot lists) at run time.

## Post-processing (canvas nodes, flat or free)

`upscaler` (Topaz 2x/4x/6x with face enhance, or SeedVR2 faithful), `video-upscale` (FLUX Precise/Creative, Topaz Precision/Starlight, up to 4K), `bg-remove`, `auto-mask` (SAM 3), `image-crop`, `image-resize`, `rotate-flip`, `color-grade` (free), `video-trim`, `video-concat` (2–10 clips), `video-frame-extract`, `merge-audio-video`, `pdf-export`.

## Choosing in one breath

- Still with text on it → GPT Image 2.5 Sunburst or Nano Banana Pro.
- Still without text, fast → Nano Banana 2.1.
- Many refs, keep product exact → Seedream 5 Pro or Nano Banana Pro.
- Any clip from a brief → Seedance 2.5.
- Animate exactly this image → Kling 3.0 (start frame) or Seedance 2.5 with `start_frame` role.
- Someone talking → Grok Imagine 1.5 or a Space with `text-to-speech` + `lipsync`.
- Need audio, captions, music, joins → build or run a Space.
