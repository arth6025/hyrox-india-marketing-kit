# Start here: the Marketing Kit for Claude

The Marketing Kit is our latest plugin: a compiled library of 79 skills. It brings together popular marketing skills from GitHub, Higgsfield's skill files and other useful frameworks for media generation, so Claude works like a creative team for product images, ads, video, motion, brand and social work. Install it once (about 5 minutes), then ask Claude for what you want.

## What's inside

| Folder | What it is |
|---|---|
| `skills/` | The 79 skills, one folder each. Claude reads these. |
| `CATALOG.md` | Every skill with what it makes, its cost and an example prompt. Read this first. |
| `workflows/` | Ready recipes: product launch, new SKU to store, paid social refresh, motion hybrid. |
| `engines/` | Five code-motion engines for rendering films on your computer (Claude Code only). |
| `references/` | Shared rules the skills read: model guide, platform specs, quality bar. |
| everything else | Docs and build scripts for whoever maintains the kit. You can ignore them. |

## Install: pick one

### A. Claude app (desktop or claude.ai): most people

1. Open Claude, then go to **Customize → Plugins → Add → Upload plugin**.
2. Choose this folder (or the zip you received).
3. Done. The plugin also syncs to Cowork and Claude Code.

### B. Claude Code (motion and video team)

Unzip this folder somewhere permanent, for example `~/marketing-kit`. Then, in Claude Code:

```
/plugin marketplace add ~/marketing-kit
/plugin install marketing-kit@shopos
```

Restart Claude Code. To pick a skill by name, type `/marketing-kit:` and choose from the list.

If you already have the older GitHub marketing skills installed, retire the four this kit replaces so Claude doesn't pick the old versions:

```
mkdir -p ~/.claude/skills-retired && mv ~/.claude/skills/{ad-creative,image,video,social} ~/.claude/skills-retired/
```

## Do I need to sign in to anything?

**For thinking work, no.** These work right away: ad concepts, ad copy and hooks, creative strategy, briefs, launch and campaign plans, motion briefs, creative test plans, performance retros and competitor teardowns.

**For anything that makes an image or a video, you sign in once.** Images and videos are made by a media generation service, and the kit already includes the connection to it. The first time you ask for a picture or clip, Claude asks you to connect: click **Connect**, sign in with your ShopOS email and pick the ShopOS workspace. You don't need to set anything up in advance.

- Claude app: if the prompt doesn't appear, go to **Customize → Plugins → Marketing Kit → Connectors → Connect**.
- Claude Code: run `/mcp`, choose the media connector, then **Authenticate**.

## Try these

1. "Ten ad concepts for our scalp serum aimed at women with hair fall" (no sign-in)
2. "What can you make with this product photo?" (free)
3. "Make a studio photo of this bottle on a clean white background"
4. "Three 4:5 ad variants for the serum, hook: wakes up a tired scalp"
5. "Animate this packshot into a 5 second loop"

You don't need skill names. Describe the outcome ("I need stuff for our Diwali sale") and Claude plans it.

## Spending

Claude always shows the price in credits and waits for your **yes** before making anything. Each person can spend up to 50 credits a day by default. Ask Arvind if you need more.

## Help

Ask Arvind for workspace access or a newer version of the kit. To update, install the newer folder the same way. Your connection is kept.
