# Workflow: hybrid motion film

Code for words, marks, UI and timing. Sloosh for matter, light, physics, music and voice. One approval per round. Runs in Claude Code or Cowork with a shell; the Sloosh steps also work in the Claude app on their own.

```
brief ─► motion-director ─► motion-plates ─► product-video / image-to-video ─► motion-film-code ─► soundtrack-and-voice ─► video-upscale-master ─► reel-export
         (none)             (low)            (medium)                         (local, none)        (medium)               (medium)              (local, none)
```

## Rounds and approvals

| Round | Skill | Credits | Approval | Output → next step |
|---|---|---|---|---|
| 0 | `brief-intake` (optional), `brand-kit-extract` | none | brief confirmed | brief + brand kit |
| 1 | `motion-director` | none | `MOTION.md` approved | beat map, shot routes, engine, Sloosh item list |
| 2 | `motion-plates` | low: drafts 1K ×3 per plate, finals 2K/4K | one approval for the draft set, one for finals | generated ids → `get_asset` → download to `films/<name>/public/sloosh/<shot-id>_<ratio>.png` |
| 3 | `product-video` / `image-to-video` / `product-animation` / `transitions-and-morphs` | medium per clip | one approval for the clip set | ids → download to `public/sloosh/<shot-id>.mp4` (transcode to 8-bit H.264 if needed) |
| 4 | `motion-film-code` (or `launch-film` for VO-led) | none | gates quoted in `NOTE.md` | `out/preview.mp4`, stills, contact sheets |
| 5 | `soundtrack-and-voice` | medium | one approval | Lyria bed / TTS as audio file (canvas) or clip with audio (Space); audio downloaded to `public/audio/` and mixed in the project, or the Space output used as is |
| 6 | optional AI pass: `video-style-transfer` (`video_edit`) | medium | one approval | host preview at https → `import_asset` → `quote_generation(mode: video_edit)` → restyled clip; keep the code master |
| 7 | `video-upscale-master` | medium | one approval | 4K master (Space `video-upscale`, clip ≤ 20 s, or chunked) |
| 8 | `reel-export` | none | | 9:16 with hook, probe report |
| 9 | `captions-subtitles` (if speech) | low | one approval | burned captions |

## Hand-off contract

Each skill ends with a handoff block (`references/brief-schema.md`):

```yaml
handoff:
  from: motion-plates
  produced:
    - {kind: generated, id: <uuid>, label: S03_hero-surface_16x9_4K, ratio: "16:9", res: 4K, model: gemini-3-pro-image-preview, seed: null}
  downloaded_to: films/arata-launch/public/sloosh/S03_hero-surface_16x9_4K.png
  suggested_next: [motion-film-code]
```

Rules:

- Sloosh → project: always `get_asset(kind: generated, id)` and download `access.url`; never a card URL. Name files by shot id.
- Project → Sloosh: the MCP cannot read a local path. Host the file at a public https URL (≤ 64 MiB) and `import_asset`, or ask the user to upload through `open_asset_upload`.
- Renders are never regenerated to retry a lost Sloosh response; reconcile with the original operation id.
- Every Sloosh item is listed in `NOTE.md` as generated and illustrative; real UI and copy are marked real.

## Where each engine sits

| Film type | Engine in round 4 | Sloosh share |
|---|---|---|
| Launch film with VO | `launch-film` (Remotion, whisper, match cuts) | plates, hero clips |
| Launch film with score | cinetic Remotion | plates, hero clips, Lyria bed |
| Logo sting, kinetic type | motionmaxxing HTML/GSAP | material still, background plate |
| Web/app demo | shotcraft Remotion template | ambient plates, multi-camera talking segment |
| Zero-npm quick promo | howseen bare HTML | plates, clips |
| No local agent | pure Sloosh: `product-animation` + `logo-animation` + `transitions-and-morphs` + `soundtrack-and-voice` | everything; type only as stills |

## Cost tiers (rough, verify with quotes)

- Plates: 1K draft ≈ cheapest tier per image; 4K hero ≈ several times a 1K image.
- Clips: 5 s Seedance 2.5 at 720p is the baseline; 1080p and longer multiply.
- Spaces: capped by `maximumReservedCredits`; LLM-heavy Spaces hold more. Compare with `remainingUnits` from `get_connection`.
- Default daily ceiling is 50 credits; a full hybrid film often needs the user to raise it at `https://sloosh.ai/settings/mcp`.

## Failure points to expect

- Product drift between a plate and its clip → regenerate the clip with the plate as `start_frame` and "keep exactly".
- Text in AI clips → never; type is code.
- Audio: the canvas has no mixer; music + VO are two merges or a local mix.
- Timing: AI clip durations snap to model ranges; cut in the project, not in Sloosh.
