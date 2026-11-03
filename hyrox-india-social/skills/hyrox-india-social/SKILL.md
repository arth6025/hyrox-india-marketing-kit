---
name: hyrox-india-social
description: Make HYROX India Instagram posts that follow the official HYROX "Social Templates Local" system — feed (3:4, 1080×1440) covers, content slides, finishers, carousels and stories (9:16) — rendered to PNG with locked layouts, the HYROX logotype, Brutal Type (or Barlow fallback), black/white/grey with yellow highlight boxes only. Use whenever someone asks for a HYROX / HYROX India post, carousel, story, race announcement, city/event post, partner or sponsor post, workout of the week, athlete quote, race-day schedule, results/stats post, recap or CTA, or hands over HYROX copy and says "design this" / "make this a post".
---

# HYROX India — social templates

**Make it yours. Keep it HYROX.** This skill fills HYROX's locked social templates with the
team's copy and photos. It never invents layouts, colours, fonts or text sizes: that is HQ's rule,
and the renderer enforces it.

```
SKILL.md
references/brand.md       ← the HYROX rules (read first, every time)
references/templates.md   ← every template, its PDF page, and its fields
scripts/make.py           ← brief.json → HTML → PNG, one per slide
scripts/render.sh         ← HTML → PNG (headless Chrome) + "copy too long" check
assets/logo/              ← HYROX logotype (white / black) + HYROX IN avatar
assets/fonts/             ← Barlow (stand-in for Brutal Type) + DM Mono
assets/samples/           ← sample race photos (for drafts and examples only)
assets/reference/         ← every template page from the HQ PDF (tNN.jpg) + guide pages
examples/briefs/ + renders/
```

## Workflow

1. **Read `references/brand.md`.** Then open the template page(s) you'll use in `assets/reference/` (e.g. `t10.jpg`).
2. **Plan the post in HYROX's 3 parts:** **cover** (World or Local) → **content** slides (as many as the story needs) → **finisher** (CTA), when needed. A single static is just a cover.
3. **Pick templates** from `references/templates.md` by purpose. If nothing fits, **don't improvise a layout**: say so and suggest a design request to HQ on Monday (that's the HYROX process).
4. **Get real inputs.** Copy as supplied (don't invent race dates, cities, prices, partners or athlete names). Photos: the team's own race photos; `assets/samples/` only for drafts. Partner logos: ask for the file (SVG/PNG, white).
5. **Write the brief** (`./hyrox-posts/<slug>.json`) and run `python3 <skill>/scripts/make.py ./hyrox-posts/<slug>.json`.
6. **If the render prints `COPY TOO LONG`, cut the copy.** Never change sizes to make it fit.
7. **Look at every PNG** and run the checklist. Fix the brief, re-render, then hand over the PNGs + brief + a caption suggestion.

## Checklist

- Black base (grey / Pain Inc. purple only for that campaign or with HQ approval). Text white; yellow only as a highlight box, never as text colour.
- HYROX logotype only in white (on dark) or black (on light); never stacked with the mark, never recoloured, never next to added text inside its exclusion zone.
- Headlines in caps, Medium weight; body left-aligned, sentence case. Single digits as 01, 02. "HYROX" always in capitals.
- Text readable on the photo (use `dim`, sparingly — "keep the background image visible and impactful").
- Story: nothing important in the top 250 px / bottom 340 px.
- Elite 15 quote templates are only for Elite 15 athletes; everyone else uses the standard quote template.
- Workout of the week: swap @HYROXWORLD for the local handle.

## Fonts

HYROX's typeface is **Brutal Type** (licensed). If it's installed on the machine, the renderer uses it automatically.
Otherwise it falls back to **Barlow** (free, closest match). Brutal Type is never bundled.

## Requirements

Python 3 and Google Chrome (or Chromium / Playwright's Chromium). Nothing else.
