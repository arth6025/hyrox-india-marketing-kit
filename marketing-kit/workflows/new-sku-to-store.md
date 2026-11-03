# Workflow: new SKU to store

From one phone photo to a complete PDP and marketplace set.

```
asset-manager (upload) ─► product-imagery (clean packshot)
   ─► product-multi-angle (5 angles) ─► white-background-compliance (marketplace main)
   ─► amazon-listing-pack (lifestyle, scale, macro, infographic)
   ─► colourway-variants (if SKU has colours)
   ─► image-to-video (5 s PDP loop) ─► upscale-and-finish (hero 4K)
   ─► collection-banner (when three SKUs exist)
```

For 10+ SKUs: `space-builder` publishes the packshot + angles canvas once; `batch-pipeline` runs it with `image-pool` or `image-input-multi` and `output_filename` `{{skuCode}}_<view>`; outputs land as a batch zip. Drafts refuse fan-out, so publish first (workspace admin).
