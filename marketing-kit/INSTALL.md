# Install

## Claude app (plugin)

1. Get `dist/sloosh-skills-2.0.0.zip` (or build it: `bash scripts/package.sh`).
2. Claude → Customize → Plugins → Add → Upload plugin → choose the zip.
3. Open the plugin's Connectors tab. Add Sloosh if it is not added, then Connect. Sign in and authorize the workspace you want to use.
4. On Team or Enterprise plans an Owner adds the Sloosh connector for the organization first.
5. Set your daily allowance and confirmation threshold at https://sloosh.ai/settings/mcp. Until you do, 50 credits/day applies.

Skills that render code on your computer (`motion-film-code`, `launch-film`, `ui-product-demo`, `animated-chart`, `reel-export`) need Claude Code or Cowork with a shell; in the Claude app they explain the Sloosh-only route instead.

## Claude Code

```bash
# from a local checkout
claude plugin add ./sloosh-skills
# or, once published to a marketplace
/plugin marketplace add shopos/sloosh-skills
/plugin install sloosh@sloosh-skills
```

Then connect the MCP (the plugin's `.mcp.json` points at `https://mcp.sloosh.ai/mcp`) and authorize your workspace when prompted. Invoke a skill as `/sloosh:<skill-id>` or just describe what you want.

For code-rendered motion also install: Node 22+, ffmpeg 6+, Python 3.11+ (numpy, scipy, soundfile, pyloudnorm, opencv-python, librosa for cinetic; numpy and Pillow for launch-film), and Chromium or Chrome Headless Shell. `motion-film-code` checks these before it starts and asks before installing anything.

## Cowork

Upload the zip as a plugin the same way as the Claude app. Connect a folder for film projects if you want renders written back to your computer.

## Connector without the plugin

Add a custom connector in Claude with the URL `https://mcp.sloosh.ai/mcp`. You get the 44 Sloosh tools without the skills.

## Verify

In a new chat: "What can Sloosh do with this product photo?" The router answers with options and spends nothing. Then: "Make a studio photo of my water bottle on white" and expect an upload card, a model choice, a quote in credits, and a request for your approval before anything is generated.

## Update

Upload a newer zip; skills are replaced in place. Your Sloosh connection and allowance stay. See `CHANGELOG.md`.
