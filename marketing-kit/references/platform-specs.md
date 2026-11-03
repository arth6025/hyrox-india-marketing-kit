# Platform specs

Sizes, lengths and safe zones per placement. Adapted from marketing-skills `ad-creative/references/platform-specs.md` and `short-form-video-specs.md`, trimmed to what Sloosh can render. Verify current platform limits before a large spend; platforms change them.

## Aspect ratio by placement

| Placement | Ratio | Px (deliver) | Notes |
|---|---|---|---|
| Instagram / Facebook feed | 4:5 | 1080×1350 | Best feed real estate. 1:1 fallback. |
| Instagram Stories / Reels, TikTok, YouTube Shorts, Snapchat | 9:16 | 1080×1920 | Keep text inside the middle 1080×1420; top 250 px and bottom 340 px get UI. |
| Facebook / LinkedIn / X feed | 1:1 | 1080×1080 | Universal fallback. |
| YouTube, landscape display, website hero | 16:9 | 1920×1080 | |
| YouTube thumbnail | 16:9 | 1280×720 | Face + 3–5 word headline, high contrast. |
| Pinterest pin | 2:3 | 1000×1500 | Vertical, text-light, lifestyle. |
| Email / WhatsApp header | 21:9 or 3:1 | 1200×400 | Short copy, product left or centre. |
| Amazon / marketplace main | 1:1 | ≥ 1600×1600 | Pure white (RGB 255), product ≥ 85% of frame, no text, no props. |
| Shopify PDP gallery | 1:1 or 4:5 | 2048×2048 | Consistent crop across SKUs. |
| LinkedIn banner | 4:1 | 1584×396 | |
| Google Display | 1.91:1, 1:1, 4:5 | 1200×628, 1200×1200, 960×1200 | |

Sloosh models render by ratio and resolution label (1K/2K/4K), not by pixel size. Pick the ratio here, `2K` for feed/story, `4K` for print or hero banners, then resize if an exact pixel size is required.

## Video length by placement

| Placement | Sweet spot | Max useful | Sound |
|---|---|---|---|
| TikTok / Reels / Shorts ad | 9–15 s | 30 s | Sound-on design; captions for sound-off. |
| Meta feed video | 6–15 s | 30 s | Most watched muted; captions. |
| YouTube bumper | 6 s | 6 s | |
| YouTube pre-roll | 15–20 s | 30 s | Brand in first 5 s. |
| Product page loop | 5–8 s | 10 s | Silent loop. |
| Website hero | 6–10 s | 15 s | Silent loop. |
| LinkedIn | 15–30 s | 60 s | Captions. |

Sloosh clip limits: most models 4–15 s per generation; Seedance 2.5 and Wan 3 up to 30 s. Longer pieces are several clips joined with `video-concat` in a Space, or a launch-film edit on the user's computer.

## Hook timing

First 1–3 seconds carry the visual action, the spoken line and the caption, and they must not repeat each other. Product visible by second 3 on paid placements. End card with offer and CTA for the last 2 seconds.

## Text on image

- Feed static: headline ≤ 6 words, one supporting line, one CTA.
- Story/Reel cover: ≤ 4 words.
- Thumbnail: 3–5 words, ≥ 90 px tall at 1280 wide.
- Models that spell well: GPT Image 2.5, Nano Banana Pro, Qwen Image 3, Ideogram 4.5. Keep each word ≤ 10 characters; verify spelling with `view_asset` before delivery.

## Compliance notes

- Before/after: both frames must be truthful; no implied medical outcomes.
- Testimonials: real reviews with permission; mark creator content as paid partnership where required.
- Faces of real people: Sloosh verifies real-person references; get consent.
- Marketplace main image: white background, no text or badges, no watermark.
