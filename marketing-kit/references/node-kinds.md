# Canvas node kinds

52 kinds from `list_node_kinds` on 2026-10-22. Short form here; call `list_node_kinds(kinds: [...])` for the config schema, pricing and examples before you wire anything. Port names below are exact.

## Inputs (become form fields when published)

| Kind | Outputs | Use |
|---|---|---|
| `prompt` | `text` | Prompt with `{{var}}` variable ports (`add-variable`). The canonical prompt source. |
| `text-input` | `text` | Static text. No ordering, so tokens inside it resolve empty. |
| `image-input` | `image` | One user image. |
| `image-input-multi` | `images` | Up to 10 images as one array. |
| `reference-image-input` | `image` | Same as image-input, semantically a style/pose reference. |
| `video-input` | `video`, `duration_seconds` | A source clip; wire duration into a video node to price its length. |
| `audio-input` | `audio` | MP3/WAV URL. |
| `document-input` | `document`, `text`, `images` | PDF/DOCX/PPTX/MD/TXT/CSV brief. |
| `url-input` | `text`, `images` | A public page: product page, brand page. No search. |
| `aspect-ratio-input` | `value` | Shared ratio control. |
| `number-input` | `value` | Number with min/max. |
| `select-input` | `value`, `prompt`, `values`, `prompts` | Dropdown; each option can carry its own prompt text. |
| `background-input`, `character-input`, `pose-input` | `images` | Curated library pickers (up to 10). |
| `image-pool` | `image` | Folder upload; one random image per run. |
| `pinterest-scraper` | `images` | Reference images for a keyword. |

## Generators (paid)

| Kind | Inputs → outputs | Pricing | Notes |
|---|---|---|---|
| `text-gen` | `prompt`, `reference_images[]`, `documents[]` → `text`, `json` | token | 18 LLM ids; `response_schema` for JSON; `system_prompt`, `temperature`. |
| `prompt-enhancer` | `prompt`, refs, docs → `text` | token | Short scene → detailed image prompt. |
| `image-gen` | `prompt`, `aspect_ratio`, `reference_images[]` → `image`, `images` | image_size | 23 models; `image_size` 1K/2K/4K; `num_images` 1–10 (Muse); `seed`; `enable_eval` + `reference_labels`. |
| `image-edit` | `image`, `prompt`, `aspect_ratio`, `reference_images[]` → `image` | image_size | Source counts toward ref limit; `adaptive` keeps framing. |
| `video-gen` | `prompt`, `first_frame`, `last_frame`, `aspect_ratio`, `duration_seconds` → `video` | by-model | `resolution` up to 4k, `generate_audio`, `negative_prompt`, `cfg_scale`, `prompt_expansion_mode`. |
| `video-reference` | `prompt`, `reference_images[]`, `reference_videos[]`, `reference_audios[]` → `video` | by-model | Adds `kling-3.0-motion-control-*`, `omnihuman-2`, `vidu-q4`. |
| `video-edit` | `video`, `prompt`, refs, audios → `video` | by-model | `task` edit/extend, `extend_seconds`. |
| `model3d-gen` | `prompt`, `image`, side views → `model` (GLB) | by-model | trellis-2, hunyuan3d, tripo, meshy, rodin, sam-3d. |
| `lyria-3` | `prompt`, refs → `audio` | flat | 30 s clip or ~2 min Pro song. |
| `text-to-speech` | `text` → `audio` | flat | 21 ElevenLabs stock voices, ≤ 1000 chars. No cloning. |
| `lipsync` | `video`, `audio` → `video` | flat | Audio ≤ 30 s. |
| `video-analyzer` | `video`, `prompt` → `text` | token | Gemini Flash/Pro. |
| `garment-classifier` | `images[]` → `class_N[]` | flat per classifier | Route garments into buckets. |

## Transforms (flat or free)

`bg-remove`, `auto-mask` (SAM 3, text-named selection → cut-out + mask), `image-crop`, `image-resize` (fill/fit/stretch), `rotate-flip`, `color-grade` (free; whole frame or one picked colour), `upscaler` (Topaz 2x/4x/6x or SeedVR2), `video-upscale` (1.5x–4x, ≤ 4K), `video-trim`, `video-concat` (2–10 clips), `video-frame-extract`, `merge-audio-video` (replaces original audio), `video-subtitle` (Veed, 30 presets, 28 languages).

## Logic

`text-iterator`, `image-iterator` (fan-out; > 16 runs warns, > 64 rejected), `bundle` (fan-in to `images[]`), `image-randomizer` (one of N per run), `router` (if/else on a value; untaken branches free), `concat` (join text parts `parts__N`).

## Outputs

`download` (browser button, no behaviour), `pdf-export` (one page per image; feeds LLM `documents`). Mark deliverables with `set-output {nodeId, include: true}`.

## Patterns that recur in the public Spaces

- **Brief → shot list → images**: `text-input` (brief) → `text-gen` (JSON shot list) → `text-iterator` → `prompt` (`{{shot}}` variable) → `image-gen` (refs: product) → `bundle` → `pdf-export`.
- **Still → clip**: `image-gen` → `video-gen.first_frame`, prompt describes motion only.
- **Two stills → morph**: `image-gen` A → `first_frame`, `image-gen` B → `last_frame` on `kling-o3` / `kling-v3-omni-video`.
- **Voiced clip**: `text-gen` (script) → `text-to-speech` → `lipsync.audio` with a face clip, or `merge-audio-video` with b-roll; `video-subtitle` last.
- **Branch by input**: `text-gen` ("is a person wearing it? yes/no") → `router.subject` → one prompt per branch → `concat` → generator.
- **Finish**: `upscaler` or `video-upscale` as the last paid node; `color-grade` for free fixes.
