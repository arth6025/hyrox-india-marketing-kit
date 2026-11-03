# Prompt grammar

How to write prompts that Sloosh models render well. Built from the Higgsfield prompt-engineering reference, marketing-skills `ai-image-prompting.md` and `ai-video-prompting.md`, and what the Sloosh Space authors do in the public catalogue. Use `enhance_prompt` (free) on anything short, show the rewrite, then quote with `enhancePrompt: false`.

## Image prompt skeleton

```
[subject with exact identity] + [what it is doing / how it sits] +
[environment] + [lighting] + [camera: lens, angle, distance] +
[style / medium / grade] + [composition and negative space for copy] +
[text to render, in quotes, verbatim] + [what must stay exact]
```

Example (product hero, Nano Banana Pro, 4:5):

> The Arata scalp serum bottle from the reference image, label facing camera, standing on wet black slate. Morning light from a window on the left, soft shadow to the right. 85 mm lens, eye level, product fills 60% of the frame, clean negative space top third. Editorial product photography, true colour, no colour cast. Keep the label text, cap shape and bottle proportions exactly as in the reference. No extra text.

Rules:

- One subject sentence first. The model weights the opening.
- Name the reference by role: "the product in reference 1", "the model in reference 2". When a model supports `reference_labels` on canvas, set them.
- Say what must not change: label, logo, colours, proportions, face.
- Put rendered text in double quotes and say "exactly". Short words spell better.
- Describe light as direction + quality + colour (left, soft, warm). Avoid "beautiful lighting".
- Camera words that work: 35 mm / 50 mm / 85 mm / macro, eye level / low angle / top-down, close-up / medium / wide.
- Negative space: say where copy will go ("empty top third").
- Avoid lists of adjectives; three precise nouns beat ten adjectives.
- Never put `{{` in a prompt sent through `quote_generation`; braces are canvas tokens.

## Video prompt skeleton

```
[shot 1: subject, action verb, camera move, duration cue] →
[shot 2 …] + [lighting and look] + [pace] + [sound if generateAudio] +
[what stays constant across shots]
```

Example (Seedance 2.5, 9:16, 10 s, audio on):

> Shot 1 (0–3 s): macro push-in on the serum dropper as one drop falls, slow motion, studio black backdrop. Shot 2 (3–7 s): cut to a woman's hand pressing the dropper onto her scalp part, bathroom window light, handheld feel. Shot 3 (7–10 s): the bottle on a marble shelf, slow orbit, label readable. Warm neutral grade throughout, soft film grain. Sound: quiet room tone, a soft drop splash, no music. Keep the bottle identical to the reference in every shot.

Rules:

- Motion verbs first: push in, orbit, pull back, rack focus, tilt up, handheld drift, whip pan. One camera move per shot.
- One action per shot; 2–4 s per shot for ads.
- For image-to-video, describe only motion and change; do not re-describe the still.
- Start/end frame models (Kling O3, Kling 3.0, Seedance): describe the transition between the two frames.
- Say "no text" or dictate exact on-screen words; models invent captions otherwise.
- Audio: say "no music" or give genre and energy; name sounds you want (pour, click, fabric).
- Keep people consistent: "the same woman as in reference 1, same hair, same top".

## Edit prompt skeleton (image-edit, video_edit)

> Change only [X]. Keep [everything else] identical: [list]. [Describe the new X precisely].

Models that respect untouched pixels: Ideogram 4.5, GPT Image 2.5 Sunburst. For video edits, Gemini Omni 1.1 Flash takes conversational instructions ("make it dusk, keep the product and camera").

## Style transfer from references

- Send 2–4 style references plus the subject reference.
- Name what to take: palette, grain, lens look, lighting, composition.
- Name what to leave: the reference's subject, logos, text.
- "Match the colour palette, contrast and film grain of references 2–4. Subject, framing and label from reference 1."

## Brand kit injection

When a brand kit exists (see `brand-kit-schema.md`), append one line:

> Brand: palette #hex, #hex; type feel: [geometric sans]; mood: [calm, clinical, warm]; never: [neon, clutter, stock-photo smiles].

## Negative prompt

Only video nodes expose `negative_prompt` (default "blur, distort, and low quality"). For images, state the positive instead ("sharp focus on the label").

## Copy inside prompts

Keep ad copy out of the image unless the placement needs it. Generate the clean plate first, then a text variant; the clean plate is reusable across languages and tests.
