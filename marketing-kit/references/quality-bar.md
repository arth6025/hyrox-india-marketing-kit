# Quality bar

What "done" means for a Sloosh deliverable, and how to check it without spending more credits.

## Check every image with `view_asset` before you call it done

Open each output (`view_asset(kind: generated, id)`; wait ~15 s after completion). Score it on five things:

| Check | Pass | Fail → fix |
|---|---|---|
| Product fidelity | Label, logo, colour, proportions match the reference | Re-quote with "keep exactly as reference 1", more refs, Seedream 5 Pro / Nano Banana Pro, or `image-edit` on the good frame |
| Text | Every word spelled right, readable at phone size | GPT Image 2.5 Sunburst or Ideogram 4.5; shorter words; text variant from a clean plate |
| Hands, faces, anatomy | Natural | Reframe to hide hands; `skin-enhancer-2`; a different seed |
| Composition | Negative space where copy goes; subject not cut by the frame | Say the layout in the prompt; `change-aspect-ratio` instead of crop |
| Brand | Palette, light and mood within the brand kit | Add `prompt_line`; `color-grade` node for small shifts |

For video, extract judgement from the card and, in a Space, a `video-analyzer` node ("list continuity errors, label legibility, product changes"). Watch for: product morphing between shots, text hallucinated on screen, extra limbs, camera drift against the brief, audio that fights the scene.

## Delivery standard

- Name every output: `brand-product-placement-concept-vN` (same string as the idempotency key).
- State ratio, resolution, seconds and whether it has audio.
- List what you checked and what you did not (e.g. "spelling verified on all three; hands on v2 slightly soft").
- Offer the next step in one line: the chaining skill, with its rough credit range.

## Credits discipline

- Draft at 1K or with Nano Banana Lite; final at 2K/4K with the hero model. Say so.
- Batch same-prompt variants with `generationCount` up to 4 instead of four quotes.
- Reuse a good still as the start frame for video instead of re-generating.
- Before a Space with LLM nodes, compare its maximum hold with `remainingUnits`.
- Never re-run on a lost response; reconcile.

## When to stop and ask

- The brief is missing the product asset.
- The quote exceeds the user's stated comfort or `fitsDailyLimit` is false.
- A real person's face is involved and consent is unclear.
- The claim on the creative needs evidence the user has not given.
- Three attempts failed the same check; show the best and explain the limit.
