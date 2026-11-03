# Creative brief object

Every generating skill works from the same brief shape. `brief-intake` builds it; other skills fill only the fields they need. Keep it in the conversation as a short block the user can correct. Never invent a field the user did not give or confirm; mark it `unknown`.

```yaml
brief:
  brand: Arata                     # name as the user writes it
  product: Scalp serum 50 ml        # one product per brief; several → several briefs
  product_assets:                   # Sloosh asset refs after upload/import
    - {kind: workspace, id: <uuid>, role: product, note: front packshot}
  brand_kit: see brand-kit-schema.md or unknown
  audience: women 25-40 in Indian metros with hair-fall worries
  objective: conversions | awareness | retention | catalogue
  offer: "Buy 2 get 1" | none
  message: the one thing the viewer should take away
  proof: review quote, stat, ingredient, award (verbatim, with source)
  tone: calm, clinical, warm            # three words max
  placements: [ig-feed-4x5, ig-story-9x16, meta-feed-1x1]
  deliverables:                          # what the user gets
    - {type: image, count: 3, ratio: "4:5"}
    - {type: video, count: 1, ratio: "9:16", seconds: 10, audio: true}
  references: [{kind: workspace, id: <uuid>, role: style|competitor|mood}]
  must_keep: [label text, cap colour, bottle shape]
  must_avoid: [neon, clutter, medical claims]
  copy_on_image: none | "exact text"
  language: en
  budget_credits: unknown | number       # user's comfort for this task
  deadline: unknown
```

## Intake questions, in order of value

Ask only what is missing and only what changes the output:

1. What is the product and do you have a photo of it? (Everything depends on the asset.)
2. Where will this run? (Decides ratios and lengths.)
3. What should it make someone do or feel? (Objective + message.)
4. Any offer or proof to show? (Copy.)
5. What must stay exact, what must never appear? (Guards.)
6. How many variations? (Credits.)

Defaults when the user says "just make it": feed 4:5 and story 9:16, three variations, no copy on image, Nano Banana Pro for stills, Seedance 2.5 for clips, 2K.

## Hand-off between skills

A skill that finishes writes a short `handoff` block:

```yaml
handoff:
  from: product-imagery
  produced:
    - {kind: generated, id: <generationId>, label: hero-4x5-v1, ratio: "4:5"}
  suggested_next: [static-ad-variants, image-to-video]
  notes: label spelling verified with view_asset
```

The next skill reads `produced` ids with `get_asset(kind: generated, id)` and passes `access.url` as references. Never pass a card URL.
