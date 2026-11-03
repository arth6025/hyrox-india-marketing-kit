# Templates and brief fields

Each template recreates a page of the HQ *Social Templates Local* PDF. Its picture is in
`assets/reference/tNN.jpg`; look at it before using the template. Worked briefs: `examples/briefs/`.

## Formats

| `format` | Size | Notes |
|---|---|---|
| `feed` (default) | 1080×1440 (3:4) | The template size. Instagram shows 3:4 in the grid. |
| `story` | 1080×1920 (9:16) | Keep text out of the top 250 px and bottom 340 px. |

## Fields every template accepts

| Field | What |
|---|---|
| `label` | Pill text, top-left: event, campaign, "HYROX INDIA", "DON'T MISS OUT" |
| `photo` | A sample name (`relay-team`, `rower-man`, `rower-woman`, `sandbag-lunges`, `sandbag-pair`, `sled-push`, `kettlebells`, `partner-portrait`) or a path to your own photo |
| `focus` | Crop focus (CSS object-position), e.g. `"50% 20%"` to keep faces in frame |
| `dim` | Picture dimming 0–0.8; use as little as needed |
| `subline` | Small line at the bottom: "Here's what's changing next season >>" |
| `logo` | `false` to hide the HYROX logotype (only where the template has none) |
| `ground` | `black` (default) · `grey` (HQ-approved only) · `pain-inc` (Pain Inc. campaign only) |

In text: `\n` = line break, `[box]TEXT[/box]` = white highlight box, `[yellow]TEXT[/yellow]` = HYROX yellow box.

**Text sizes are locked.** The renderer allows ≤8% squeeze, then prints `COPY TOO LONG`: shorten the copy.

## Covers (step 1)

| Template | PDF page | Use | Fields |
|---|---|---|---|
| `cover` | t09–t12 | Headline on black, photo across the lower half. The everyday Local cover. | `headline`, `align` (`left`/`center`/`right`), `photo` |
| `cover-full` | t21–t22, t46 (story) | Full-bleed photo, headline bottom-left (story: centred). World-style or race moments. | `headline`, `body` (optional short paragraph), `logo_on_photo` |
| `cover-sandwich` | t08, t13 | Headline / photo / headline, centred. | `headline`, `headline2`, `photo` |
| `event` | t17 | City event lockup: presenting partner + HYROX + CITY. | `partner` (name) or `partner_logo` (file), `city`, `subline` (dates) |
| `partner` | t16, t19 | Partner announcement: partner, rule, HYROX, role; optional photo. | `partner` / `partner_logo`, `role` ("NATIONAL PARTNER"), `photo` |

## Content (step 2)

| Template | PDF page | Use | Fields |
|---|---|---|---|
| `photo-text` | t18, t20 | Headline + date/city row + photo. News, race info. | `headline`, `date` ("26.11.26"), `city`, `photo`, `inset` (false = full width) |
| `text` | t23 | Big statement + three ruled notes. | `statement`, `notes` [3 strings] |
| `subheads` | t24, t58 (story) | Headline + highlight-box subheadings, one line each. Explainers, rules, FAQs. | `headline`, `items` [{`title`,`text`}] |
| `stats` | t35 (full-bleed) / t36 (inset) | Big numbers with highlight labels: results, times, participants. | `headline`, `stats` [{`label`,`value`}], `photo`, `full_photo` |
| `schedule` | t37 | Race-day schedule: date/time + activity. | `headline`, `rows` [{`date`,`time`,`activity`}] |
| `quote` | t07 (long) / t31 (short, `short: true`) | Partner / founder / athlete quote. **Not for Elite 15** (they have their own templates). | `partner`, `name`, `quote`, `photo`, `short` |
| `checklist` | t26 | Do / don't, what to bring, yes / no. | `headline`, `yes`, `no`, `yes_title`, `no_title` |
| `list` | t49 (story "INSIDE") | Numbered 01–04 over a photo. | `headline` ("INSIDE"), `items` [4 strings], `photo` |

## Finisher (step 3)

| Template | PDF page | Use | Fields |
|---|---|---|---|
| `cta` | t42–t43, t45, t65 (story) | Centred call to action, optional button pill and photo. | `headline`, `button`, `subline`, `photo` |

## Not built (request from HQ, or use the PDF in InDesign)

Bar/donut charts (t25, t27, t32), multi-partner logo grids (t29), Elite 15 quote templates, World Championship /
Performance event graphics, city logos (always from HQ's City Logos folder).

## Recipes

- **Race announcement:** `event` → `photo-text` (date, city, what's new) → `cta` ("REGISTER NOW").
- **How HYROX works:** `cover-full` ("8 STATIONS. 8 KM. ONE RACE.") → `subheads` (Run / stations) → `stats` → `cta`.
- **Partner reveal:** `partner` → `quote` (`short: true`) → `photo-text`.
- **Race-day story set:** `cover-full` → `list` ("INSIDE") → `schedule` → `cta`.
- **Results / recap:** `cover` ("TIME FOR RECAP") → `stats` (`full_photo`) → `cta`.
