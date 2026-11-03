# Canvas blueprints

Operation lists for `apply_canvas_operations`, used by `space-builder` and `batch-pipeline`. Each file is a JSON array of operations in the shapes the canvas guide documents (`add-node`, `configure-node`, `connect`, `add-variable`, `set-output`, ...). Node and edge ids inside are placeholders; mint fresh `nd_`/`eg_` ULIDs per draft and re-read port names from `list_node_kinds(kinds: [...])` before applying, because node schemas change.

| File | Builds | Notes |
|---|---|---|
| `product-to-three-scenes-pdf.json` | image-input → prompt ×3 → image-gen ×3 → pdf-export | runs as a draft (no fan-out) |
| `brief-to-shot-list-fanout.json` | text-input (brief) → text-gen (JSON shot list) → text-iterator → prompt → image-gen → bundle → pdf-export | fan-out: publish before running; a draft run refuses it |

Add a blueprint per reusable recipe you publish, and reference it from the skill that uses it.
