# Workflow: product launch kit

One product, one week, every asset a launch needs. Run by `campaign-orchestrator` as rounds; each round is one approval.

```
R0 (free)   brief-intake ─► brand-kit-extract ─► creative-strategy ─► ad-concepts ─► motion-director
R1 (low)    product-imagery (hero ×3, 4:5 + 16:9) ─► product-multi-angle
R2 (med)    static-ad-variants (3 concepts × 4:5 + 9:16) ─► sale-banner-set (if offer)
R3 (med)    image-to-video (PDP loop) ─► cinematic-product-film (keyframes) 
R4 (high)   cinematic-product-film (shots) ─► ugc-video-ad ─► captions-subtitles
R5 (var)    motion-plates ─► motion-film-code or launch-film (local) ─► soundtrack-and-voice
R6 (low)    platform-content-pack ─► youtube-thumbnail ─► email-header
R7 (free)   brand-consistency-check ─► creative-testing-plan ─► launch-campaign-plan
```

Hand-offs: every round writes a handoff block with generated ids; the next round resolves them with `get_asset`. Start frames for R3 come from R1 heroes. R5 downloads R1–R4 outputs into the film project and brings the render back with `import_asset` only if an AI restyle pass is wanted.

Budget: check `get_connection.budget.remainingUnits` before each round; a Space with LLM nodes (UGC) can hold more than a day's allowance; split across days or raise the ceiling in settings.
