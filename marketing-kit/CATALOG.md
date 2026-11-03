# Sloosh skill catalog

79 skills · plugin 2.0.0 · generated 2026-10-22 by `scripts/build_registry.py`. Status legend: **Ready** = verified MCP tools only · **Ready (public Space)** = depends on a published Space verified by id · **Needs validation** = tool path exists, end-to-end run not yet observed · **Needs local agent** = runs in Claude Code or Cowork with a shell · **Proposed** = needs an MCP or product change (see docs/GAP-ANALYSIS.md).

| Status | Count |
|---|---|
| Ready | 27 |
| Ready (public Space) | 42 |
| Needs validation | 5 |
| Needs local agent | 5 |

## Orchestration and intake

| Skill | Tier | Status | Cost | What it makes | Try saying |
|---|---|---|---|---|---|
| [`asset-manager`](skills/asset-manager/SKILL.md) | 1 | Ready | none | Get images and videos into and out of the Sloosh workspace: upload local files through the upload card, import public URLs, find existing workspace or generated assets, resolve a generated id to a usable URL, look at an asset, and name things so later skills can find them | “Use the serum photo I uploaded yesterday” |
| [`brief-intake`](skills/brief-intake/SKILL.md) | 1 | Ready | none | Turn a vague creative request into the shared Sloosh brief object (product, assets, audience, objective, placements, deliverables, must-keep, must-avoid) that every generating skill reads | “I need something for our Diwali sale” |
| [`campaign-orchestrator`](skills/campaign-orchestrator/SKILL.md) | 1 | Ready | variable | Run a multi-skill Sloosh plan as rounds, one approval per round, so a launch, a sale or a content pack gets its images, ads, clips and motion pieces in the right order and within the daily credit allowance | “Run the whole launch kit for the new sneaker” |
| [`creative-iteration`](skills/creative-iteration/SKILL.md) | 1 | Ready | low | Improve a Sloosh result the user has seen: fix one thing with an edit, re-roll with what worked kept, change the model, reuse a seed, or go back a step, with the cheapest path first | “The label is misspelled on the second one, fix just that” |
| [`sloosh-router`](skills/sloosh-router/SKILL.md) | 1 | Ready | none | Pick the right Sloosh skill or chain of skills for a creative or marketing request and hand off with a short brief | “I need stuff for our Diwali sale” |

## Image generation and editing

| Skill | Tier | Status | Cost | What it makes | Try saying |
|---|---|---|---|---|---|
| [`background-swap-relight`](skills/background-swap-relight/SKILL.md) | 1 | Ready (public Space) | low | Put an existing product or person into a new setting and relight them so they look shot there: a described scene, a supplied scene photo, or the light of a reference photo | “Put this candle on a marble bathroom counter with window light” |
| [`image-edit-retouch`](skills/image-edit-retouch/SKILL.md) | 1 | Ready | low | Change one thing in an existing image and keep the rest: remove an object or the background, fix a label, swap a colour, clean skin, add or remove a prop, extend a surface | “Remove the price tag from this photo” |
| [`product-imagery`](skills/product-imagery/SKILL.md) | 1 | Ready | low | Make product photos with Sloosh, such as studio packshots, lifestyle scenes, hero shots and scene or background changes of the user's own product images | “Make a studio photo of my water bottle on a clean white background” |
| [`product-multi-angle`](skills/product-multi-angle/SKILL.md) | 1 | Ready (public Space) | medium | Turn one product photo into a matching set of angles (front, three-quarter, side, back, top-down) with shape, colours and logo kept identical, for PDP galleries, marketplaces and 360-style sets | “Give me the back and side of this bottle” |
| [`reframe-outpaint`](skills/reframe-outpaint/SKILL.md) | 1 | Ready (public Space) | low | Change an image's aspect ratio or canvas size without cropping the subject: outpaint a photo to 16:9 or 9:16, extend a background, or rebuild a finished ad layout for a new format | “Make this landscape shot work as a 9:16 story” |
| [`style-reference-transfer`](skills/style-reference-transfer/SKILL.md) | 1 | Ready (public Space) | low | Shoot the user's product or subject in the look of reference images or a video frame: palette, grade, lighting, lens, set and mood taken from the references, product and label taken from the user's photo | “Shoot our serum like this Aesop campaign” |
| [`colourway-variants`](skills/colourway-variants/SKILL.md) | 2 | Ready (public Space) | low | Show the same product in other colours or finishes with shape, hardware, texture and lighting unchanged, for colourway previews, pre-sampling decisions and PDP swatches | “Show this tote in black, navy and sand” |
| [`moodboard-exploration`](skills/moodboard-exploration/SKILL.md) | 2 | Ready (public Space) | low | Explore visual directions cheaply before committing: a moodboard of 4 to 9 small images from a mood description, a 3x3 variation grid of one product photo, or several camera angles of one scene, all on low-cost models | “Show me a few directions for a calm, clinical skincare look” |
| [`upscale-and-finish`](skills/upscale-and-finish/SKILL.md) | 2 | Ready (public Space) | low | Deliver a final image at print or hero size: upscale 2x to 6x with Topaz or SeedVR2, optional face enhancement, a tonal pass and the right file format | “Make this hero image 4K for the homepage” |

## Performance advertising

| Skill | Tier | Status | Cost | What it makes | Try saying |
|---|---|---|---|---|---|
| [`ad-concepts`](skills/ad-concepts/SKILL.md) | 1 | Ready | none | Turn a product, an audience and proof into a ranked set of ad concepts, each a testable hypothesis (segment, motivation, angle, format) with a visual direction and the Sloosh skill that produces it | “Give me ten ad concepts for our scalp serum aimed at women with hair fall” |
| [`ad-copy-variations`](skills/ad-copy-variations/SKILL.md) | 1 | Ready | none | Write ad copy at volume for Meta, TikTok, Google, LinkedIn and Pinterest from a concept and real customer language: hook matrices with visual, spoken and caption columns, awareness-stage headlines, primary text, descriptions and CTAs within platform limits, each with a falsifiable test hypothesis | “Write 10 hooks for the serum ad aimed at hair fall” |
| [`ad-hook-matrix`](skills/ad-hook-matrix/SKILL.md) | 1 | Ready (public Space) | medium | Test three hooks at once by running the Sloosh "Ad Hook Test Matrix" Space, which turns one product photo and three headlines into a grid of studio, lifestyle and handheld ad creatives, then map the results to a one-variable test | “Test these three hooks for the serum on a grid of ad images” |
| [`sale-banner-set`](skills/sale-banner-set/SKILL.md) | 1 | Ready (public Space) | low | Make a matching set of sale and offer banners with Sloosh in square, portrait, story and landscape from one product photo and the offer text, through the "Sale & Offer Banner Set" Space or a direct per-ratio render | “Sale banners for 30% off the serum, all sizes” |
| [`static-ad-variants`](skills/static-ad-variants/SKILL.md) | 1 | Ready | variable | Make sets of static ad images with Sloosh for paid social and display, in feed and story sizes, from a product photo plus a concept, hook or offer; a clean plate first, then text variants with legible headlines | “Create three 9:16 ad variants for my summer sale on this sneaker” |
| [`before-after-ad`](skills/before-after-ad/SKILL.md) | 2 | Ready (public Space) | low | Make a split-screen before/after ad with Sloosh from a product photo and the problem it solves, through the "Before / After Ad" Space or a direct two-panel render, with truthful frames and compliant copy | “Before and after ad for our scalp serum, problem is flaky itchy scalp” |
| [`comparison-ad`](skills/comparison-ad/SKILL.md) | 2 | Ready (public Space) | low | Make an "us vs them" comparison ad with Sloosh from a product photo and four to six real comparison points, through the "Us vs Them Comparison" Space or a direct render with a check/cross table | “Us vs them ad for our greens powder against typical multivitamins” |
| [`creative-testing-plan`](skills/creative-testing-plan/SKILL.md) | 2 | Ready | none | Turn a batch of Sloosh ad outputs into a creative test plan: one variable per comparison, a naming convention that matches the generation idempotency keys, ad-set mapping, metrics and thresholds, run length and what each outcome decides next | “How should we test these six variants?” |
| [`reference-ad-remix`](skills/reference-ad-remix/SKILL.md) | 2 | Ready (public Space) | low | Borrow a proven ad layout for your own product with Sloosh: swap your product into a reference ad, recompose a finished design into new formats, get a nine-concept grid from one photo, or a headline poster, through the Spaces "Swap Product into a Reference Ad", "Design Recomposer", "3x3 Product Ad Grid" and "Product Poster / Ad Creative" | “Make an ad like this one but with our bottle” |
| [`testimonial-ads`](skills/testimonial-ads/SKILL.md) | 2 | Ready (public Space) | low | Turn real customer reviews into testimonial ad images with Sloosh, through the "Review Card Creatives" Space (three reviews, three matching cards) or a direct render, with the quote verbatim and the product in frame | “Make testimonial ads from these three reviews of the serum” |

## AI video

| Skill | Tier | Status | Cost | What it makes | Try saying |
|---|---|---|---|---|---|
| [`captions-subtitles`](skills/captions-subtitles/SKILL.md) | 1 | Ready (public Space) | low | Burn word-accurate captions or styled subtitles into a video with Sloosh, through the Add Captions Space or a canvas subtitle node with presets, fonts, position and 28 languages | “Add captions to this Reel” |
| [`cinematic-product-film`](skills/cinematic-product-film/SKILL.md) | 1 | Ready | high | Plan and make a multi-shot cinematic product film with Sloosh, from storyboard to keyframes to generated shots, with continuity across shots | “Make a 30 second cinematic film for our new perfume” |
| [`image-to-video`](skills/image-to-video/SKILL.md) | 1 | Ready | medium | Animate one exact still into a short clip with Sloosh, keeping the frame as it is and adding only motion, such as a PDP loop, a slow orbit or a turntable | “Animate this packshot into a 5 second loop for the product page” |
| [`product-video`](skills/product-video/SKILL.md) | 1 | Ready | medium | Make one short product video clip with Sloosh from a prompt, with or without a product image as reference or start frame | “Make a 5 second clip of my candle flickering on a wooden table, vertical” |
| [`ugc-video-ad`](skills/ugc-video-ad/SKILL.md) | 1 | Ready (public Space) | high | Make a creator-style UGC video ad with Sloosh from product photos and a creator photo, using the published UGC Spaces, such as a selfie-style ad with voiceover, an unboxing clip or a product-in-hand still | “Make a UGC ad for my face serum with this creator photo, 15 seconds, Hindi” |
| [`motion-replicate`](skills/motion-replicate/SKILL.md) | 2 | Ready (public Space) | high | Recreate the movement of a reference video with your own character, creator or product in Sloosh, by motion transfer, object swap or character swap, using the Shadow Clone, character replicator and trending-video swap Spaces or a motion-control canvas | “Recreate this dance video with our mascot” |
| [`talking-head-video`](skills/talking-head-video/SKILL.md) | 2 | Ready (public Space) | medium | Make a person on video say a script with Sloosh, by voicing and lip-syncing an existing clip, dubbing it into another language, re-shooting it from several camera angles, or generating a speaking clip from a photo with native audio | “Make this clip of our founder say the new 20 second pitch” |
| [`ugc-storyboard`](skills/ugc-storyboard/SKILL.md) | 2 | Ready | high | Plan a short UGC-style product video as a storyboard, then make its shots as separate Sloosh images or clips in two approved rounds, or run a published UGC Space when one fits | “Write a UGC storyboard for my face serum and make the shots” |
| [`video-extend-edit`](skills/video-extend-edit/SKILL.md) | 2 | Ready | medium | Make an existing clip longer or change it with a prompt in Sloosh, such as adding five seconds past the last frame, changing the lighting, removing an object or swapping the setting while the product and camera stay | “Extend this 5 second clip so the bottle keeps turning for 5 more seconds” |
| [`video-style-transfer`](skills/video-style-transfer/SKILL.md) | 2 | Ready (public Space) | medium | Restyle an existing video with Sloosh while the product, its motion and the camera stay the same, such as a new setting around a turntable clip, a reference colour grade, a relight, an anime or film look | “Put this turntable clip in a Diwali living room instead of the studio” |
| [`video-upscale-master`](skills/video-upscale-master/SKILL.md) | 2 | Ready (public Space) | medium | Upscale a finished clip to 1080p, 2K or 4K with Sloosh and state the delivery specs, through the Video Upscale Space or a canvas upscale node with FLUX or Topaz models | “Upscale this clip to 4K” |

## Motion design

| Skill | Tier | Status | Cost | What it makes | Try saying |
|---|---|---|---|---|---|
| [`launch-film`](skills/launch-film/SKILL.md) | 1 | Needs local agent | variable | Direct and render a premium SaaS or product launch film in Remotion on the user's computer, from voiceovers, reference videos, brand assets, a website URL and a local SFX library, with match cuts on every scene change, 3D website fly-overs, kinetic type, SFX cue sheets and mastered 1080p or 4K delivery | “Make a 30-second launch film for our app from PART 1.mp3 and our website” |
| [`logo-animation`](skills/logo-animation/SKILL.md) | 1 | Ready (public Space) | medium | Make a logo reveal, sting or lockup with Sloosh: the 3D Logo Animation Space, a textured-logo still animated into a clip, a direct start-frame reveal, or a start-to-end lockup morph, and route to a code build when the mark must stay vector-sharp | “Animate our logo as a 5-second intro” |
| [`motion-director`](skills/motion-director/SKILL.md) | 1 | Ready | none | Turn a request for a motion piece (launch video, promo, logo sting, kinetic type, feature loop, product animation, explainer) into a MOTION brief with one idea, a beat map on a timing grid, a shot list that marks each shot as code-rendered or Sloosh-generated, the copy, the sound plan and the engine route | “We need a 20-second launch video for our new app” |
| [`motion-film-code`](skills/motion-film-code/SKILL.md) | 1 | Needs local agent | variable | Build and render a motion graphics film from code on the user's computer (Remotion, HyperFrames or plain HTML seek(t)) using the vendored engines, with Sloosh supplying plates, product clips, music, voice, restyles and upscales | “Build the launch film from this MOTION brief with Remotion” |
| [`motion-plates`](skills/motion-plates/SKILL.md) | 1 | Ready | low | Generate the still plates a motion film needs with Sloosh: backgrounds, hero surfaces, textures, product cut-outs with transparent background, 3D-looking hero renders, logos in a material, and consistent plate sets in 16:9 and 9:16 at up to 4K, named and exported for a code engine | “Make the four background plates from this MOTION brief in 16:9 and 9:16” |
| [`product-animation`](skills/product-animation/SKILL.md) | 1 | Ready (public Space) | medium | Animate a product with Sloosh's published motion Spaces (feature callout orbit, exploded view, 360 orbit, zero-gravity float, tear-away reveal, splash and pour, stop-motion unpack, crush and squish, it's cake, cardboard world, multishot clips, product placement video) or a custom Seedance move, keeping the label exact | “Make an exploded view animation of our earbuds” |
| [`soundtrack-and-voice`](skills/soundtrack-and-voice/SKILL.md) | 1 | Ready (public Space) | medium | Add music, a voiceover or lip-synced speech to a clip with Sloosh: the Add a Soundtrack Space, a canvas with Lyria 3 music, ElevenLabs stock text-to-speech, merge-audio-video and lipsync, or the Talking Clip Space, with sound-sync rules for cuts, ducking and silence before the payoff | “Put a calm piano bed under this product clip” |
| [`animated-chart`](skills/animated-chart/SKILL.md) | 2 | Needs local agent | low | Make an animated chart, count-up number, milestone reveal or before-and-after stat as a looping clip built in code so every value stays exactly as given, with Sloosh supplying a background plate or a static infographic still | “Animate our Q3 results: 12k, 18k, 31k, 44k orders” |
| [`kinetic-typography`](skills/kinetic-typography/SKILL.md) | 2 | Needs validation | low | Make text-led motion: kinetic type promos, animated headlines, word reveals and typographic end cards, from code when the words must be exact and from Sloosh when a short A-to-B text morph or a typographic poster still is enough | “Kinetic type promo for the Diwali sale, 12 seconds, 9:16” |
| [`motion-effects-library`](skills/motion-effects-library/SKILL.md) | 2 | Ready | none | Find the right motion effect, shot recipe or transition for a moment and return where its recipe lives and how to make it, from 124 shotcraft shot cards, 16 charlie motion effects, the cinetic technique and seam catalogue, and the Sloosh-only approximations when no code renderer is available | “What is a good opening shot for a SaaS promo where the product shows through the title?” |
| [`reel-export`](skills/reel-export/SKILL.md) | 2 | Needs local agent | none | Turn a finished horizontal or square motion video into a 1080x1920 Reel, TikTok or Short that uploads cleanly, with a two-line hook and logos inside the safe zone, H.264, yuv420p, limited range, BT.709, faststart and a silent audio track when there is no sound, checked with ffprobe; stills reframe through Sloosh | “Make this landscape promo a Reel with the hook 'This launch / is 100% code'” |
| [`reference-to-motion`](skills/reference-to-motion/SKILL.md) | 2 | Ready (public Space) | variable | Turn a reference video, reel or ad the user admires into a style guide and shot list for their own brand, then either a MOTION brief for a code build or an AI recreation through Sloosh (video analysis in a canvas, motion transfer with Shadow Clone, character motion replication, or product-plus-reference-video ad) | “Make a reel like this one for our serum” |
| [`transitions-and-morphs`](skills/transitions-and-morphs/SKILL.md) | 2 | Needs validation | medium | Make a clip that travels from one still to another with Sloosh start-frame and end-frame video models, for scene transitions, before-and-after, pose-to-pose, colourway and day-to-dusk morphs, and plan match cuts between shots | “Morph the packshot from the black colourway to the sand one” |
| [`ui-product-demo`](skills/ui-product-demo/SKILL.md) | 2 | Needs local agent | low | Make an app or website demo film from real screenshots with 2.5D camera moves, cursor and interaction shots, beat-synced cuts and sound, built in Remotion from the video-shotcraft template and cards, with Sloosh adding ambient plates and a multi-camera talking segment | “Turn our dashboard into a 30-second product video” |

## Brand identity

| Skill | Tier | Status | Cost | What it makes | Try saying |
|---|---|---|---|---|---|
| [`brand-consistency-check`](skills/brand-consistency-check/SKILL.md) | 1 | Ready | none | Review finished Sloosh images against the brand kit (palette, photography, typography, never-list, logo use) and return a pass/fix table that names the skill to fix each miss | “Check these six ad images against our brand kit before we post” |
| [`brand-kit-extract`](skills/brand-kit-extract/SKILL.md) | 1 | Ready | none | Build a reusable brand kit (palette hexes, type feel, photography and motion rules, voice, never-list, one prompt line) from the user's brand guide, website or logo, so every other Sloosh skill renders on-brand | “Here is our brand guide PDF, use it for everything we make today” |
| [`brand-board`](skills/brand-board/SKILL.md) | 2 | Ready (public Space) | medium | Make a visual brand board with Sloosh from a logo, business details and colour preferences: palette page, typography ideas, mood scenes and a logo lockup page as images | “Make a brand board for Arata with our logo and forest green” |
| [`logo-from-brief`](skills/logo-from-brief/SKILL.md) | 2 | Ready (public Space) | low | Make logo concepts with Sloosh from a brand name, a short description, a style and colours, as raster images (PNG) with variations, then refine the chosen one | “Logo ideas for Arata, a scalp care brand, calm and clinical, forest green” |
| [`merch-packaging-mockups`](skills/merch-packaging-mockups/SKILL.md) | 2 | Ready (public Space) | medium | Put an existing logo or artwork onto merchandise, packaging, stationery, labels and out-of-home scenes with Sloosh: caps and tees, pouches and bottles, a folded box from a dieline, business cards, magazine cover, billboard and poster scenes | “Show our logo on a cap, a tote and a hoodie” |
| [`brand-icon-set`](skills/brand-icon-set/SKILL.md) | 3 | Ready (public Space) | low | Make a matching set of brand icons with Sloosh from a logo and a list of icon names, in the logo's colours and stroke style, as one 3x3 sheet or individual tiles | “Nine icons for our PDP: shipping, returns, vegan, cruelty-free, dermatologist, 30-day, recyclable, made in India, paraben-free” |
| [`social-profile-kit`](skills/social-profile-kit/SKILL.md) | 3 | Ready (public Space) | low | Make a coordinated set of social profile assets with Sloosh from a logo and brand colours: profile image, Instagram highlight covers, and banners sized for LinkedIn, X, YouTube and Facebook | “Set up our Instagram and LinkedIn profiles with our logo and colours” |

## Social content

| Skill | Tier | Status | Cost | What it makes | Try saying |
|---|---|---|---|---|---|
| [`platform-content-pack`](skills/platform-content-pack/SKILL.md) | 1 | Ready (public Space) | medium | Turn one approved hero image into a matched set for every placement with Sloosh, in 4:5, 1:1, 9:16, 16:9 and 2:3, by outpainting the same picture or regenerating it per ratio with the same references | “Give me this hero in every size for Instagram, TikTok and YouTube” |
| [`reels-shorts-clip`](skills/reels-shorts-clip/SKILL.md) | 1 | Ready (public Space) | medium | Make a vertical 9:16 clip of up to 15 seconds for Instagram Reels, TikTok and YouTube Shorts with Sloosh, from a product photo or an approved still, with a hook in the first 3 seconds, captions and an optional soundtrack | “Make a Reel for the new candle, 9 seconds, with captions” |
| [`seasonal-creatives`](skills/seasonal-creatives/SKILL.md) | 1 | Ready (public Space) | medium | Refresh product creatives for a festival, holiday or season with Sloosh, such as Diwali, Christmas, Eid, Holi, Valentine's, Black Friday or summer, as stills and short clips with the product kept exact | “Diwali versions of our gift box ad, feed and story” |
| [`carousel-builder`](skills/carousel-builder/SKILL.md) | 2 | Ready (public Space) | medium | Make a swipe-through carousel for Instagram or LinkedIn with Sloosh, 4 to 10 slides in one art direction with a cover that works alone, from a product photo and the story to tell | “Make a 5-slide carousel about why our serum is different” |
| [`email-header`](skills/email-header/SKILL.md) | 2 | Ready (public Space) | low | Make wide email and WhatsApp campaign headers with Sloosh, plus a matching square graphic, from a product photo, a campaign mood and a short message | “Email header for our Diwali sale, 20% off, with the gift box” |
| [`youtube-thumbnail`](skills/youtube-thumbnail/SKILL.md) | 2 | Ready (public Space) | low | Make truthful, high-contrast YouTube thumbnails and vertical video covers with Sloosh, with a kept face, a 3 to 5 word headline and controlled variants that each test one change | “Thumbnail for my video: I tested 5 scalp serums for 30 days” |

## E-commerce and catalogue

| Skill | Tier | Status | Cost | What it makes | Try saying |
|---|---|---|---|---|---|
| [`amazon-listing-pack`](skills/amazon-listing-pack/SKILL.md) | 1 | Ready (public Space) | medium | Make a marketplace listing image set with Sloosh from one product photo: a compliant white-background main image plus secondary images (lifestyle, in-hand scale, macro detail, feature infographic, what's in the box) | “Amazon images for our scalp serum: main, lifestyle, size in hand, close-up, a features image” |
| [`virtual-try-on`](skills/virtual-try-on/SKILL.md) | 1 | Ready (public Space) | low | Show a garment, eyewear or jewellery on a person with Sloosh, keeping the person, pose and background and the product's real colour and fit; also move a person into a new pose | “Put this kurta on the model in photo 2, keep her pose” |
| [`white-background-compliance`](skills/white-background-compliance/SKILL.md) | 1 | Ready (public Space) | low | Make a marketplace-compliant white-background product image with Sloosh: product isolated, pure white behind it, filling the frame, no text or props | “Put this kettle on a pure white background for Amazon” |
| [`collection-banner`](skills/collection-banner/SKILL.md) | 2 | Ready (public Space) | low | Make a wide store or collection banner with Sloosh from two to four product photos arranged on one set, with clear space left for a headline, for Shopify homepages, collection pages and email heroes | “Homepage banner with our three serums on one shelf, text goes on the left” |
| [`fashion-lookbook-set`](skills/fashion-lookbook-set/SKILL.md) | 2 | Ready (public Space) | high | Make a consistent fashion lookbook or catalogue set with Sloosh: the same model wearing the garment across studio poses, editorial locations, contact sheets and short lookbook clips, optionally bundled as a PDF | “Shoot this kurta on a model: hero, three poses, one detail, studio grey” |
| [`food-photo-studio`](skills/food-photo-studio/SKILL.md) | 2 | Ready (public Space) | low | Turn a phone snap of a dish, drink or packaged food into commercial food photography with Sloosh: cleaned plating, studio or natural light, menu, delivery-app and social sizes | “Make this biryani photo look like a menu shot” |
| [`ghost-mannequin`](skills/ghost-mannequin/SKILL.md) | 2 | Ready (public Space) | low | Turn on-model or mannequin garment photos into invisible-mannequin product shots on white with Sloosh, keeping shape, colour and details, including front, back and inside-neck views | “Ghost mannequin front and back for this kurta from the model shots” |
| [`product-in-room`](skills/product-in-room/SKILL.md) | 2 | Ready (public Space) | low | Place furniture, decor or home products into a real room photo with Sloosh at the right scale and light, or restyle a room around a product | “Show this three-seater in my living room photo, against the back wall” |

## Creative strategy and analysis

| Skill | Tier | Status | Cost | What it makes | Try saying |
|---|---|---|---|---|---|
| [`creative-strategy`](skills/creative-strategy/SKILL.md) | 1 | Ready | none | Turn a brief into three to five creative territories, each with a visual world, a hook family, the proof it leans on, the Sloosh skills that produce it and a credit tier, so a team can pick a direction before spending | “Give me creative directions for the serum launch” |
| [`launch-campaign-plan`](skills/launch-campaign-plan/SKILL.md) | 1 | Ready | none | Plan a product launch or campaign as phases with an asset list per phase, each asset mapped to the Sloosh skill that makes it, its inputs and credit tier, plus a week-by-week calendar and the approval rounds | “Plan the creative for our serum launch on 15 November” |
| [`competitor-creative-teardown`](skills/competitor-creative-teardown/SKILL.md) | 2 | Ready | none | Tear down competitor ads and content the user pastes or uploads (ad library screenshots, reels, PDP images) by hook, format, proof, offer, visual world and likely funnel role, then turn the patterns into concepts and remix briefs for Sloosh without copying logos, characters or copy | “Here are 8 ads from our competitor's ad library, what are they doing?” |
| [`creative-performance-retro`](skills/creative-performance-retro/SKILL.md) | 2 | Ready | none | Read the user's ad results table (by creative name, with hook rate, hold rate, CTR, CVR, CPA or spend) and decide per creative whether to kill, scale or iterate, diagnose where in the funnel each one lost, and brief the next Sloosh round with the skill that makes it | “Here are last week's numbers for the six variants, what do we do?” |
| [`shopify-store-audit`](skills/shopify-store-audit/SKILL.md) | 2 | Needs validation | none | Audit a Shopify or D2C storefront's visual merchandising and creative assets (hero, collection banners, PDP galleries, ratios and consistency, missing video, lifestyle, UGC and social proof) from its URL when the host can read the web, or from screenshots the user pastes, and return a prioritized fix list where every fix names the Sloosh skill that produces the asset | “Audit our Shopify store's product images and tell me what's missing” |

## Canvas and Space authoring

| Skill | Tier | Status | Cost | What it makes | Try saying |
|---|---|---|---|---|---|
| [`published-spaces`](skills/published-spaces/SKILL.md) | 1 | Ready | variable | Find, quote and run a published Sloosh Space, a ready-made recipe such as an ad grid, a UGC video ad, a catalogue pack, a logo reveal or a try-on, and follow its run through checkpoints to the outputs | “Run the UGC Selfie Video Ad Space on my product” |
| [`space-builder`](skills/space-builder/SKILL.md) | 1 | Needs validation | variable | Build a reusable Sloosh workflow as a canvas from a goal, test it with one draft run, and publish it as a workspace Space with a clean form: product → scene set → PDF, brief → shot list → images, still → clip → captions, and similar pipelines | “Build a Space that takes a product photo and gives me three scene shots and a PDF” |
| [`batch-pipeline`](skills/batch-pipeline/SKILL.md) | 2 | Needs validation | high | Run the same Sloosh workflow over many inputs (every SKU, every colour, every scene) with iterators, bundles, image pools, named output files and a PDF contact sheet, sized to stay within fan-out limits and the daily allowance | “Run the white-background packshot on all 40 SKUs” |
| [`prompt-enhancer-workflow`](skills/prompt-enhancer-workflow/SKILL.md) | 2 | Ready | none | Turn a short or vague image or video idea into a detailed, model-specific prompt the user can see and edit before anything is quoted, using Sloosh's free enhance_prompt plus the shared prompt grammar | “Improve this prompt: bottle on table nice light” |

## Common chains

```
ad-concepts                      → ad-copy-variations
ad-concepts                      → static-ad-variants
ad-concepts                      → ad-hook-matrix
ad-concepts                      → before-after-ad
ad-concepts                      → comparison-ad
ad-concepts                      → testimonial-ads
ad-concepts                      → reference-ad-remix
ad-concepts                      → ugc-video-ad
ad-concepts                      → creative-testing-plan
ad-copy-variations               → static-ad-variants
ad-copy-variations               → ad-hook-matrix
ad-copy-variations               → ugc-video-ad
ad-copy-variations               → ugc-storyboard
ad-copy-variations               → sale-banner-set
ad-copy-variations               → creative-testing-plan
ad-hook-matrix                   → static-ad-variants
ad-hook-matrix                   → creative-testing-plan
ad-hook-matrix                   → ugc-video-ad
amazon-listing-pack              → upscale-and-finish
amazon-listing-pack              → product-multi-angle
amazon-listing-pack              → image-to-video
amazon-listing-pack              → brand-consistency-check
animated-chart                   → reel-export
animated-chart                   → motion-film-code
animated-chart                   → platform-content-pack
asset-manager                    → product-imagery
asset-manager                    → static-ad-variants
asset-manager                    → product-video
asset-manager                    → image-to-video
asset-manager                    → published-spaces
asset-manager                    → brand-kit-extract
asset-manager                    → upscale-and-finish
background-swap-relight          → static-ad-variants
background-swap-relight          → image-to-video
background-swap-relight          → upscale-and-finish
background-swap-relight          → platform-content-pack
batch-pipeline                   → published-spaces
batch-pipeline                   → upscale-and-finish
batch-pipeline                   → platform-content-pack
before-after-ad                  → static-ad-variants
before-after-ad                  → creative-testing-plan
before-after-ad                  → reframe-outpaint
brand-board                      → brand-icon-set
brand-board                      → social-profile-kit
brand-board                      → merch-packaging-mockups
brand-board                      → product-imagery
brand-board                      → upscale-and-finish
brand-consistency-check          → image-edit-retouch
brand-consistency-check          → background-swap-relight
brand-consistency-check          → static-ad-variants
brand-consistency-check          → reframe-outpaint
brand-consistency-check          → creative-iteration
brand-icon-set                   → social-profile-kit
brand-icon-set                   → amazon-listing-pack
brand-icon-set                   → static-ad-variants
brand-icon-set                   → upscale-and-finish
brand-icon-set                   → image-edit-retouch
brand-kit-extract                → product-imagery
brand-kit-extract                → static-ad-variants
brand-kit-extract                → logo-from-brief
brand-kit-extract                → brand-board
brand-kit-extract                → brand-consistency-check
brand-kit-extract                → motion-director
brand-kit-extract                → platform-content-pack
brand-kit-extract                → campaign-orchestrator
brief-intake                     → campaign-orchestrator
brief-intake                     → asset-manager
brief-intake                     → brand-kit-extract
brief-intake                     → creative-strategy
brief-intake                     → product-imagery
brief-intake                     → static-ad-variants
brief-intake                     → product-video
brief-intake                     → motion-director
campaign-orchestrator            → product-imagery
campaign-orchestrator            → static-ad-variants
campaign-orchestrator            → cinematic-product-film
campaign-orchestrator            → image-to-video
campaign-orchestrator            → platform-content-pack
campaign-orchestrator            → motion-director
campaign-orchestrator            → creative-testing-plan
campaign-orchestrator            → creative-iteration
captions-subtitles               → video-upscale-master
captions-subtitles               → reel-export
captions-subtitles               → creative-testing-plan
carousel-builder                 → platform-content-pack
carousel-builder                 → creative-testing-plan
carousel-builder                 → image-to-video
cinematic-product-film           → soundtrack-and-voice
cinematic-product-film           → captions-subtitles
cinematic-product-film           → video-upscale-master
cinematic-product-film           → launch-film
cinematic-product-film           → space-builder
cinematic-product-film           → reel-export
collection-banner                → static-ad-variants
collection-banner                → reframe-outpaint
collection-banner                → email-header
collection-banner                → upscale-and-finish
collection-banner                → image-to-video
colourway-variants               → platform-content-pack
colourway-variants               → static-ad-variants
colourway-variants               → carousel-builder
colourway-variants               → batch-pipeline
comparison-ad                    → static-ad-variants
comparison-ad                    → creative-testing-plan
competitor-creative-teardown     → ad-concepts
competitor-creative-teardown     → reference-ad-remix
competitor-creative-teardown     → comparison-ad
competitor-creative-teardown     → creative-strategy
competitor-creative-teardown     → ugc-video-ad
creative-iteration               → upscale-and-finish
creative-iteration               → image-edit-retouch
creative-iteration               → video-extend-edit
creative-iteration               → campaign-orchestrator
creative-performance-retro       → ad-concepts
creative-performance-retro       → static-ad-variants
creative-performance-retro       → ugc-video-ad
creative-performance-retro       → ad-copy-variations
creative-performance-retro       → creative-strategy
creative-performance-retro       → creative-testing-plan
creative-strategy                → ad-concepts
creative-strategy                → moodboard-exploration
creative-strategy                → launch-campaign-plan
creative-strategy                → cinematic-product-film
creative-strategy                → motion-director
creative-strategy                → platform-content-pack
creative-strategy                → testimonial-ads
creative-testing-plan            → creative-performance-retro
creative-testing-plan            → ad-concepts
email-header                     → platform-content-pack
email-header                     → creative-testing-plan
fashion-lookbook-set             → reels-shorts-clip
fashion-lookbook-set             → platform-content-pack
fashion-lookbook-set             → static-ad-variants
fashion-lookbook-set             → carousel-builder
fashion-lookbook-set             → upscale-and-finish
fashion-lookbook-set             → brand-consistency-check
fashion-lookbook-set             → batch-pipeline
food-photo-studio                → static-ad-variants
food-photo-studio                → platform-content-pack
food-photo-studio                → image-to-video
food-photo-studio                → carousel-builder
food-photo-studio                → upscale-and-finish
ghost-mannequin                  → white-background-compliance
ghost-mannequin                  → virtual-try-on
ghost-mannequin                  → fashion-lookbook-set
ghost-mannequin                  → amazon-listing-pack
ghost-mannequin                  → colourway-variants
ghost-mannequin                  → upscale-and-finish
image-edit-retouch               → upscale-and-finish
image-edit-retouch               → static-ad-variants
image-edit-retouch               → background-swap-relight
image-to-video                   → captions-subtitles
image-to-video                   → video-extend-edit
image-to-video                   → video-upscale-master
image-to-video                   → reels-shorts-clip
image-to-video                   → platform-content-pack
kinetic-typography               → motion-film-code
kinetic-typography               → transitions-and-morphs
kinetic-typography               → soundtrack-and-voice
kinetic-typography               → reel-export
kinetic-typography               → static-ad-variants
launch-campaign-plan             → campaign-orchestrator
launch-campaign-plan             → ad-concepts
launch-campaign-plan             → product-imagery
launch-campaign-plan             → static-ad-variants
launch-campaign-plan             → cinematic-product-film
launch-campaign-plan             → motion-director
launch-campaign-plan             → platform-content-pack
launch-campaign-plan             → sale-banner-set
launch-campaign-plan             → email-header
launch-campaign-plan             → creative-testing-plan
launch-film                      → video-upscale-master
launch-film                      → reel-export
launch-film                      → captions-subtitles
launch-film                      → soundtrack-and-voice
logo-animation                   → motion-film-code
logo-animation                   → soundtrack-and-voice
logo-animation                   → video-upscale-master
logo-animation                   → reel-export
logo-animation                   → transitions-and-morphs
logo-from-brief                  → brand-board
logo-from-brief                  → brand-icon-set
logo-from-brief                  → social-profile-kit
logo-from-brief                  → merch-packaging-mockups
logo-from-brief                  → logo-animation
logo-from-brief                  → image-edit-retouch
logo-from-brief                  → upscale-and-finish
merch-packaging-mockups          → upscale-and-finish
merch-packaging-mockups          → platform-content-pack
merch-packaging-mockups          → image-to-video
merch-packaging-mockups          → product-animation
moodboard-exploration            → style-reference-transfer
moodboard-exploration            → product-imagery
moodboard-exploration            → creative-strategy
moodboard-exploration            → motion-director
motion-director                  → motion-film-code
motion-director                  → launch-film
motion-director                  → motion-plates
motion-director                  → product-animation
motion-director                  → logo-animation
motion-director                  → kinetic-typography
motion-director                  → transitions-and-morphs
motion-director                  → soundtrack-and-voice
motion-director                  → motion-effects-library
motion-director                  → ui-product-demo
motion-director                  → animated-chart
motion-effects-library           → motion-film-code
motion-effects-library           → product-animation
motion-effects-library           → transitions-and-morphs
motion-effects-library           → kinetic-typography
motion-effects-library           → logo-animation
motion-effects-library           → image-to-video
motion-film-code                 → soundtrack-and-voice
motion-film-code                 → video-upscale-master
motion-film-code                 → video-style-transfer
motion-film-code                 → reel-export
motion-film-code                 → captions-subtitles
motion-plates                    → motion-film-code
motion-plates                    → launch-film
motion-plates                    → image-to-video
motion-plates                    → transitions-and-morphs
motion-plates                    → upscale-and-finish
motion-plates                    → kinetic-typography
motion-plates                    → animated-chart
motion-replicate                 → captions-subtitles
motion-replicate                 → video-upscale-master
motion-replicate                 → reels-shorts-clip
platform-content-pack            → image-to-video
platform-content-pack            → carousel-builder
platform-content-pack            → email-header
platform-content-pack            → creative-testing-plan
product-animation                → captions-subtitles
product-animation                → soundtrack-and-voice
product-animation                → video-upscale-master
product-animation                → motion-film-code
product-animation                → reels-shorts-clip
product-animation                → video-extend-edit
product-imagery                  → static-ad-variants
product-imagery                  → image-to-video
product-imagery                  → upscale-and-finish
product-imagery                  → platform-content-pack
product-imagery                  → product-multi-angle
product-in-room                  → static-ad-variants
product-in-room                  → image-to-video
product-in-room                  → colourway-variants
product-in-room                  → upscale-and-finish
product-in-room                  → platform-content-pack
product-multi-angle              → white-background-compliance
product-multi-angle              → amazon-listing-pack
product-multi-angle              → product-animation
product-multi-angle              → upscale-and-finish
product-multi-angle              → platform-content-pack
product-video                    → captions-subtitles
product-video                    → video-extend-edit
product-video                    → video-upscale-master
product-video                    → reels-shorts-clip
product-video                    → soundtrack-and-voice
prompt-enhancer-workflow         → product-imagery
prompt-enhancer-workflow         → product-video
prompt-enhancer-workflow         → image-to-video
prompt-enhancer-workflow         → static-ad-variants
prompt-enhancer-workflow         → cinematic-product-film
prompt-enhancer-workflow         → space-builder
published-spaces                 → creative-iteration
published-spaces                 → upscale-and-finish
published-spaces                 → captions-subtitles
published-spaces                 → platform-content-pack
reel-export                      → captions-subtitles
reel-export                      → reels-shorts-clip
reels-shorts-clip                → captions-subtitles
reels-shorts-clip                → soundtrack-and-voice
reels-shorts-clip                → youtube-thumbnail
reels-shorts-clip                → creative-testing-plan
reels-shorts-clip                → reel-export
reference-ad-remix               → static-ad-variants
reference-ad-remix               → creative-testing-plan
reference-ad-remix               → reframe-outpaint
reference-to-motion              → motion-director
reference-to-motion              → motion-film-code
reference-to-motion              → motion-replicate
reference-to-motion              → product-video
reference-to-motion              → ugc-storyboard
reference-to-motion              → space-builder
reframe-outpaint                 → platform-content-pack
reframe-outpaint                 → upscale-and-finish
reframe-outpaint                 → image-to-video
sale-banner-set                  → email-header
sale-banner-set                  → platform-content-pack
sale-banner-set                  → reframe-outpaint
sale-banner-set                  → creative-testing-plan
seasonal-creatives               → sale-banner-set
seasonal-creatives               → email-header
seasonal-creatives               → reels-shorts-clip
seasonal-creatives               → platform-content-pack
seasonal-creatives               → video-style-transfer
shopify-store-audit              → product-imagery
shopify-store-audit              → product-multi-angle
shopify-store-audit              → white-background-compliance
shopify-store-audit              → collection-banner
shopify-store-audit              → image-to-video
shopify-store-audit              → testimonial-ads
shopify-store-audit              → ugc-video-ad
shopify-store-audit              → platform-content-pack
shopify-store-audit              → creative-strategy
shopify-store-audit              → launch-campaign-plan
sloosh-router                    → brief-intake
sloosh-router                    → campaign-orchestrator
sloosh-router                    → product-imagery
sloosh-router                    → static-ad-variants
sloosh-router                    → product-video
sloosh-router                    → motion-director
sloosh-router                    → brand-kit-extract
sloosh-router                    → published-spaces
social-profile-kit               → reframe-outpaint
social-profile-kit               → upscale-and-finish
social-profile-kit               → platform-content-pack
social-profile-kit               → image-edit-retouch
soundtrack-and-voice             → captions-subtitles
soundtrack-and-voice             → video-upscale-master
soundtrack-and-voice             → reel-export
soundtrack-and-voice             → motion-film-code
space-builder                    → published-spaces
space-builder                    → batch-pipeline
space-builder                    → creative-iteration
static-ad-variants               → creative-testing-plan
static-ad-variants               → image-to-video
static-ad-variants               → platform-content-pack
static-ad-variants               → reframe-outpaint
static-ad-variants               → brand-consistency-check
static-ad-variants               → upscale-and-finish
style-reference-transfer         → static-ad-variants
style-reference-transfer         → image-to-video
style-reference-transfer         → platform-content-pack
style-reference-transfer         → motion-plates
talking-head-video               → captions-subtitles
talking-head-video               → video-upscale-master
talking-head-video               → reels-shorts-clip
testimonial-ads                  → static-ad-variants
testimonial-ads                  → carousel-builder
testimonial-ads                  → creative-testing-plan
transitions-and-morphs           → motion-film-code
transitions-and-morphs           → launch-film
transitions-and-morphs           → video-extend-edit
transitions-and-morphs           → soundtrack-and-voice
transitions-and-morphs           → video-upscale-master
transitions-and-morphs           → batch-pipeline
ugc-storyboard                   → captions-subtitles
ugc-storyboard                   → talking-head-video
ugc-storyboard                   → reels-shorts-clip
ugc-storyboard                   → space-builder
ugc-video-ad                     → captions-subtitles
ugc-video-ad                     → creative-testing-plan
ugc-video-ad                     → reels-shorts-clip
ugc-video-ad                     → video-extend-edit
ui-product-demo                  → soundtrack-and-voice
ui-product-demo                  → captions-subtitles
ui-product-demo                  → video-upscale-master
ui-product-demo                  → reel-export
ui-product-demo                  → launch-film
upscale-and-finish               → platform-content-pack
upscale-and-finish               → reframe-outpaint
video-extend-edit                → captions-subtitles
video-extend-edit                → video-upscale-master
video-extend-edit                → video-style-transfer
video-style-transfer             → captions-subtitles
video-style-transfer             → video-upscale-master
video-style-transfer             → seasonal-creatives
video-upscale-master             → reel-export
video-upscale-master             → platform-content-pack
virtual-try-on                   → fashion-lookbook-set
virtual-try-on                   → static-ad-variants
virtual-try-on                   → image-to-video
virtual-try-on                   → reels-shorts-clip
virtual-try-on                   → upscale-and-finish
virtual-try-on                   → brand-consistency-check
white-background-compliance      → amazon-listing-pack
white-background-compliance      → upscale-and-finish
white-background-compliance      → product-multi-angle
white-background-compliance      → image-to-video
white-background-compliance      → static-ad-variants
youtube-thumbnail                → creative-testing-plan
youtube-thumbnail                → platform-content-pack
```
