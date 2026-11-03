# Brand kit object

Built by `brand-kit-extract`, consumed by every skill through the "Brand:" line in `prompt-grammar.md`. Store it in the conversation; in Claude Code or Cowork also save it as `brand-kit.yaml` next to the user's assets so later sessions reuse it.

```yaml
brand_kit:
  name: Arata
  source: https://arata.in            # or "user supplied" or "logo only"
  extracted_on: 2026-10-22
  logo_assets:
    - {kind: workspace, id: <uuid>, variant: primary, background: light}
    - {kind: workspace, id: <uuid>, variant: mono-white, background: dark}
  palette:
    primary: {hex: "#1F3A2E", name: forest, use: backgrounds, type}
    secondary: {hex: "#E8DCC8", name: sand, use: cards}
    accent: {hex: "#C8553D", name: terracotta, use: CTA, highlights}
    neutrals: ["#FFFFFF", "#111111"]
  typography:
    headline: {feel: geometric sans, example: "Söhne-like", weight: medium, case: sentence}
    body: {feel: humanist sans}
    on_image_text: allowed | sparingly | never
  photography:
    light: soft directional daylight, no hard flash
    palette_bias: warm neutral, muted greens
    composition: generous negative space, product off-centre
    people: real-looking, Indian, 25-40, no stock smiles
    textures: stone, linen, botanicals
  motion:
    pace: slow, considered
    moves: push-in, slow orbit, rack focus
    transitions: cuts, no wipes
    sound: room tone, no music beds unless asked
  voice:
    tone: [calm, clinical, warm]
    say: [scalp-first, dermatologist-tested]
    never_say: [miracle, cure, instant]
  never:
    - neon colours
    - cluttered sets
    - medical claims
    - text over the product label
  prompt_line: "Brand: forest #1F3A2E, sand #E8DCC8, terracotta accent #C8553D; geometric sans; calm, clinical, warm; soft daylight; never neon, clutter or claims."
```

## How skills use it

- Append `prompt_line` to every image and video prompt.
- Pass `logo_assets` as references when the logo must appear; say "logo exactly as reference N, no redraw".
- Use `palette` hexes verbatim for backgrounds and on-image text; models read hex codes.
- `brand-consistency-check` scores outputs against `palette`, `photography` and `never`.

## Extraction sources, in order

1. The user's own brand guide (upload as `document-input` in a canvas, or paste).
2. The website (`url-input` node, or read it in Claude with web access): colours from CSS variables and hero sections, type from headings, photography from the first ten product images.
3. The logo alone: `palette-from-moodboard-images` Space for a palette card, then confirm with the user.

Always show the extracted kit to the user before you rely on it; extraction is a guess until confirmed.
