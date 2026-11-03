#!/usr/bin/env python3
"""HYROX India post builder: fills the locked HYROX social templates with your copy and photos.

    python3 make.py brief.json          # writes HTML + PNG per slide (and warns if copy is too long)
    python3 make.py brief.json --html   # HTML only

Brief = JSON. Top-level keys apply to every slide; each slide can override.

{
  "format": "feed",                 # feed 1080x1440 (3:4, the template size) | story 1080x1920
  "out": "out/round-up",            # file prefix relative to the brief; carousels add -1, -2 ...
  "slides": [
    {"template": "cover", "label": "HYROX INDIA", "headline": "RACE WITH YOUR FRIENDS", "photo": "relay-team",
     "subline": "HYROX RELAYS >>"}
  ]
}

Templates (see references/templates.md): cover, cover-full, cover-sandwich, event, partner, photo-text,
text, subheads, stats, schedule, quote, checklist, list, cta.
HYROX rule: replace copy and imagery only. Layouts, fonts, colours and text sizes are locked.
"""
import html, json, os, re, subprocess, sys

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(SKILL, "assets")
FORMATS = {"feed": (1080, 1440), "story": (1080, 1920)}
GROUNDS = {"black": "#000000", "grey": "#313335",
           "pain-inc": "linear-gradient(100deg,#5d4a6c 0%,#7f6590 55%,#9a77a8 100%)"}


def url(p):
    return "file://" + os.path.abspath(p).replace(" ", "%20")


def esc(s):
    return html.escape(str(s or ""))


def rich(s):
    """Escape; \\n = line break; [box]text[/box] = white highlight box; [yellow]text[/yellow] = HYROX yellow box."""
    s = esc(s).replace("\\n", "\n")
    s = re.sub(r"\[box\](.+?)\[/box\]", r'<span class="hl">\1</span>', s)
    s = re.sub(r"\[yellow\](.+?)\[/yellow\]", r'<span class="hl y">\1</span>', s)
    return s.replace("\n", "<br>")


def image(v, base):
    if not v:
        return None
    samples = os.path.join(A, "samples")
    for f in sorted(os.listdir(samples)):
        if f.startswith(v):
            return url(os.path.join(samples, f))
    p = v if os.path.isabs(v) else os.path.join(base, os.path.expanduser(v))
    if not os.path.exists(p):
        sys.exit(f"Image not found: {v}")
    return url(p)


def fonts_css():
    f = os.path.join(A, "fonts")
    # Brutal Type is HYROX's licensed font: used automatically when installed; Barlow is the free stand-in
    return f"""
@font-face{{font-family:HX;src:local("Brutal Type Regular"),local("BrutalType-Regular"),url({url(f+'/Barlow-Regular.ttf')});font-weight:400}}
@font-face{{font-family:HX;src:local("Brutal Type Medium"),local("BrutalType-Medium"),url({url(f+'/Barlow-Medium.ttf')});font-weight:500}}
@font-face{{font-family:HX;src:local("Brutal Type Bold"),local("BrutalType-Bold"),url({url(f+'/Barlow-SemiBold.ttf')});font-weight:700}}
@font-face{{font-family:HXMono;src:url({url(f+'/DMMono-Medium.ttf')})}}
"""


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:var(--W);height:var(--H);overflow:hidden;background:#000}
.c{position:relative;width:var(--W);height:var(--H);overflow:hidden;background:var(--ground);color:#fff;font-family:HX,sans-serif;font-weight:400}
.abs{position:absolute}
.photo{position:absolute;object-fit:cover}
.dim{position:absolute;inset:0;pointer-events:none}
.logo{position:absolute;width:calc(var(--u)*150);top:calc(var(--u)*70);right:var(--m)}
.logo img{width:100%;display:block}
.pill{position:absolute;top:calc(var(--u)*64);left:var(--m);border:calc(var(--u)*1.6) solid #fff;padding:calc(var(--u)*3) calc(var(--u)*9);
      font:500 calc(var(--u)*15)/1.15 HX;letter-spacing:.09em;text-transform:uppercase;white-space:nowrap}
.hd{font-weight:500;text-transform:uppercase;line-height:.93;letter-spacing:.004em}
.sub{position:absolute;left:var(--m);bottom:calc(var(--u)*52);font:400 calc(var(--u)*22)/1.2 HX;letter-spacing:.02em}
.body{font:400 calc(var(--u)*26)/1.45 HX}
.hl{background:#fff;color:#000;padding:0 calc(var(--u)*5);font-weight:500;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.hl.y{background:#FFED00}
.mono{font-family:HXMono,monospace}
.rule{height:calc(var(--u)*1.6);background:#fff}
.fit{display:block}
"""

FIT_JS = """
<script>
// HYROX templates keep fixed text sizes. Allow at most 8% shrink, then flag the box as too long.
document.fonts.ready.then(()=>{document.querySelectorAll('.fit').forEach(el=>{
  const box=el.parentElement; let s=parseFloat(getComputedStyle(el).fontSize); const min=s*0.92;
  // compare real positions: tight caps poke a few px past the line box, which scrollHeight counts as overflow
  const over=()=>{const e=el.getBoundingClientRect(), b=box.getBoundingClientRect(), t=s*0.12;
    return el.scrollWidth>el.clientWidth+2 || e.top<b.top-t || e.bottom>b.bottom+t;};
  while(over()&&s>min){s-=1;el.style.fontSize=s+'px'}
  if(over()) el.setAttribute('data-overflow', el.dataset.name||'text');
});});
</script>
"""


def logo(s, pos="tr"):
    if s.get("logo", True) is False:
        return ""
    col = "black" if s.get("ground") == "white" else "white"
    st = ""
    if pos == "tc":
        st = 'style="right:auto;left:50%;transform:translateX(-50%)"'
    return f'<div class="logo" {st}><img src="{url(os.path.join(A, "logo", f"hyrox_{col}.png"))}" alt="HYROX"></div>'


def pill(s, key="label", style=""):
    return f'<div class="pill" style="{style}">{esc(s[key])}</div>' if s.get(key) else ""


def sub(s, style=""):
    return f'<div class="sub" style="{style}">{rich(s["subline"])}</div>' if s.get("subline") else ""


def dim(level, side="bottom"):
    if not level:
        return ""
    to = {"bottom": "top", "top": "bottom", "full": None}[side]
    if to is None:
        return f'<div class="dim" style="background:rgba(0,0,0,{level})"></div>'
    return f'<div class="dim" style="background:linear-gradient(to {to},rgba(0,0,0,{level}) 0%,rgba(0,0,0,0) 60%)"></div>'


def hd(text, size, name="headline", align="left", style=""):
    return (f'<div class="hd fit" data-name="{name}" style="font-size:calc(var(--u)*{size});text-align:{align};{style}">'
            f'{rich(text)}</div>')


# ---------------- templates ----------------
# Each mirrors a page of the HYROX "Social Templates Local" PDF (page numbers in references/templates.md).

def T_cover(s, b, W, H, u, m):
    """Headline on black, photo across the lower half. p09-p12."""
    al = s.get("align", "left")
    ph = image(s.get("photo"), b)
    top = 0.47 if H < 1600 else 0.42
    return f"""
<img class="photo" src="{ph}" style="left:0;top:{H*top}px;width:{W}px;height:{H*(1-top)}px;object-position:{s.get('focus','50% 30%')}">
{dim(s.get('dim', .45), 'bottom')}
<div class="abs" style="left:{m}px;right:{m}px;top:{150*u}px;height:{H*top-170*u}px">{hd(s.get('headline',''), s.get('size',166), align=al)}</div>
{pill(s)}{logo(s)}{sub(s)}"""


def T_cover_full(s, b, W, H, u, m):
    """Full-bleed photo, headline bottom-left, optional body. p21-p22, p45-p47 (story)."""
    ph = image(s.get("photo"), b)
    body = f'<div class="body" style="margin-top:{22*u}px;max-width:{560*u}px">{rich(s["body"])}</div>' if s.get("body") else ""
    return f"""
<img class="photo" src="{ph}" style="inset:0;width:100%;height:100%;object-position:{s.get('focus','50% 40%')}">
{dim(s.get('dim', .55), 'bottom')}
<div class="abs" style="left:{m}px;right:{m}px;bottom:{(130 if not s.get('subline') else 120)*u}px;max-height:{H*0.55}px;display:flex;flex-direction:column;justify-content:flex-end">
  {hd(s.get('headline',''), s.get('size',150 if H > 1600 else 136), align=s.get('align','center' if H > 1600 else 'left'))}{body}</div>
{pill(s)}{logo(s) if s.get('logo_on_photo') else ''}{sub(s)}"""


def T_cover_sandwich(s, b, W, H, u, m):
    """Headline top + photo + headline bottom, centred. p08, p13."""
    ph = image(s.get("photo"), b)
    return f"""
<img class="photo" src="{ph}" style="left:{W*0.07}px;top:{H*0.2}px;width:{W*0.86}px;height:{H*0.55}px;object-position:{s.get('focus','50% 35%')}">
<div class="abs" style="left:{m}px;right:{m}px;top:{110*u}px;height:{H*0.2}px">{hd(s.get('headline',''), s.get('size',150), align='center')}</div>
<div class="abs" style="left:{m}px;right:{m}px;top:{H*0.68}px;height:{H*0.28}px">{hd(s.get('headline2',''), s.get('size',150), 'headline2', 'center')}</div>
{pill(s)}{logo(s)}"""


def T_event(s, b, W, H, u, m):
    """Event lockup: presenting partner + HYROX + CITY. p17."""
    partner = ""
    if s.get("partner_logo"):
        partner = f'<img src="{image(s["partner_logo"], b)}" style="max-width:{430*u}px;max-height:{90*u}px;display:block;margin:0 auto {48*u}px">'
    elif s.get("partner"):
        partner = f'<div style="font:700 italic calc(var(--u)*44)/1 HX;margin-bottom:{44*u}px">{esc(s["partner"])}</div>'
    city = " ".join(esc(s.get("city", "INDIA")).upper())
    return f"""
<div class="abs" style="left:0;right:0;top:{H*0.33}px;text-align:center">
  {partner}
  <img src="{url(os.path.join(A,'logo','hyrox_white.png'))}" style="width:{560*u}px;display:block;margin:0 auto">
  <div style="font:400 calc(var(--u)*92)/1 HX;letter-spacing:.24em;margin:{52*u}px 0 0 .24em">{city}</div>
</div>
{pill(s, style='left:50%;transform:translateX(-50%)')}{sub(s, 'left:0;right:0;text-align:center')}"""


def T_partner(s, b, W, H, u, m):
    """Partner announcement: partner + rule + HYROX + role, optional photo below. p16, p19."""
    ph = image(s.get("photo"), b)
    top = H * (0.16 if ph else 0.3)
    partner = (f'<img src="{image(s["partner_logo"], b)}" style="max-width:{460*u}px;max-height:{140*u}px;display:block;margin:0 auto">'
               if s.get("partner_logo") else f'<div style="font:700 calc(var(--u)*64)/1 HX">{esc(s.get("partner","PARTNER"))}</div>')
    photo = (f'<img class="photo" src="{ph}" style="left:0;top:{H*0.5}px;width:{W}px;height:{H*0.5}px;object-position:{s.get("focus","50% 30%")}">'
             + dim(.35, 'bottom')) if ph else ""
    return f"""{photo}
<div class="abs" style="left:0;right:0;top:{top}px;text-align:center">
  {partner}
  <div class="rule" style="width:{380*u}px;margin:{44*u}px auto {48*u}px"></div>
  <img src="{url(os.path.join(A,'logo','hyrox_white.png'))}" style="width:{380*u}px;display:block;margin:0 auto">
  <div style="font:500 calc(var(--u)*17)/1 HX;letter-spacing:.14em;margin-top:{30*u}px;text-transform:uppercase">{esc(s.get('role','NATIONAL PARTNER'))}</div>
</div>
{pill(s, style='left:50%;transform:translateX(-50%)')}{sub(s, 'left:0;right:0;text-align:center')}"""


def T_photo_text(s, b, W, H, u, m):
    """Headline top-left, optional date/city row, photo, subline. p18, p20."""
    ph = image(s.get("photo"), b)
    meta = ""
    if s.get("date") or s.get("city"):
        meta = (f'<div class="abs mono" style="left:{m}px;right:{m}px;top:{H*0.335}px;display:flex;justify-content:space-between;'
                f'font-size:{28*u}px"><span>{esc(s.get("date",""))}</span><span style="font-family:HX;font-weight:500">{esc(s.get("city","")).upper()}</span></div>')
    right = W * (0.82 if s.get("inset", True) else 1)
    return f"""
<img class="photo" src="{ph}" style="left:0;top:{H*0.37}px;width:{right}px;height:{H*0.43}px;object-position:{s.get('focus','50% 35%')}">
<div class="abs" style="left:{m}px;right:{m}px;top:{150*u}px;height:{H*0.2}px">{hd(s.get('headline',''), s.get('size',122))}</div>
{meta}{pill(s)}{logo(s)}{sub(s)}"""


def T_text(s, b, W, H, u, m):
    """Statement text + three ruled notes. p23."""
    notes = "".join(f'<div style="display:flex;gap:{28*u}px;align-items:flex-start;margin-top:{34*u}px">'
                    f'<div class="rule" style="width:{230*u}px;margin-top:{14*u}px;flex:none"></div>'
                    f'<div style="font:400 calc(var(--u)*22)/1.4 HX">{rich(n)}</div></div>' for n in s.get("notes", []))
    return f"""
<div class="abs" style="left:{m}px;right:{m*1.6}px;top:{150*u}px;height:{H*0.4}px">
  <div class="fit" data-name="statement" style="font:500 calc(var(--u)*{s.get('size',62)})/1.12 HX">{rich(s.get('statement',''))}</div></div>
<div class="abs" style="left:{m}px;right:{m}px;bottom:{150*u}px">{notes}</div>
{pill(s)}{sub(s)}"""


def T_subheads(s, b, W, H, u, m):
    """Headline + subheading highlight boxes with one line each. p24, p58 (story)."""
    items = "".join(f'<div style="margin-top:{36*u}px"><span class="hl" style="font-size:{38*u}px">{esc(i.get("title",""))}</span>'
                    f'<div style="font:400 calc(var(--u)*32)/1.35 HX;margin-top:{8*u}px">{rich(i.get("text",""))}</div></div>'
                    for i in s.get("items", []))
    return f"""
<div class="abs" style="left:{m}px;right:{m}px;top:{150*u}px;height:{H*0.2}px">{hd(s.get('headline',''), s.get('size',84))}</div>
<div class="abs" style="left:{m}px;right:{m}px;bottom:{130*u}px">{items}</div>
{pill(s)}{sub(s, 'left:auto;right:var(--m)')}"""


def T_stats(s, b, W, H, u, m):
    """Big numbers with highlight-box labels over a photo. p35 (full-bleed) / p36 (inset photo)."""
    ph = image(s.get("photo"), b)
    full = s.get("full_photo", True)
    stats = s.get("stats", [])
    if full:
        bg = f'<img class="photo" src="{ph}" style="inset:0;width:100%;height:100%;object-position:{s.get("focus","50% 40%")}">' + dim(.6, 'full')
        blocks = "".join(f'<div style="margin-top:{40*u}px"><span class="hl" style="font-size:{36*u}px">{esc(x.get("label",""))}</span>'
                         f'<div style="font:500 calc(var(--u)*220)/1 HX;margin-top:{12*u}px;letter-spacing:.01em">{esc(x.get("value",""))}</div></div>' for x in stats)
        return f"""{bg}
<div class="abs" style="left:{m}px;right:{m}px;top:{150*u}px;height:{H*0.2}px">{hd(s.get('headline',''), s.get('size',124))}</div>
<div class="abs" style="left:{m}px;right:{m}px;bottom:{90*u}px">{blocks}</div>{pill(s)}"""
    cols = "".join(f'<div><span class="hl" style="font-size:{30*u}px">{esc(x.get("label",""))}</span>'
                   f'<div style="font:500 calc(var(--u)*140)/1 HX;margin-top:{14*u}px">{esc(x.get("value",""))}</div></div>' for x in stats)
    return f"""
<img class="photo" src="{ph}" style="left:{m}px;top:{150*u}px;width:{W-2*m}px;height:{H*0.48}px;object-position:{s.get('focus','50% 35%')}">
<div class="abs" style="left:{m}px;right:{m}px;bottom:{80*u}px;display:flex;gap:{70*u}px">{cols}</div>{pill(s)}"""


def T_schedule(s, b, W, H, u, m):
    """Headline + date/time/activity rows. p37."""
    rows = "".join(f'<div style="display:flex;gap:{48*u}px;margin-top:{26*u}px;font-size:{27*u}px;line-height:1.2">'
                   f'<div class="mono" style="width:{190*u}px;flex:none">{esc(r.get("date",""))}<br>{esc(r.get("time",""))}</div>'
                   f'<div>{rich(r.get("activity",""))}</div></div>' for r in s.get("rows", []))
    return f"""
<div class="abs" style="left:{m}px;right:{m}px;top:{150*u}px;height:{H*0.3}px">{hd(s.get('headline',''), s.get('size',140))}</div>
<div class="abs" style="left:{m}px;right:{m}px;bottom:{90*u}px">{rows}</div>{pill(s)}"""


def T_quote(s, b, W, H, u, m):
    """Partner header line, name in a highlight box, quote. p07 (long quote) / p31 (short quote + photo)."""
    ph = image(s.get("photo"), b)
    head = (f'<div class="abs" style="left:{m}px;right:{m}px;top:{62*u}px;display:flex;justify-content:space-between;'
            f'font:500 calc(var(--u)*15)/1 HX;letter-spacing:.2em">'
            f'<span>H Y R O X</span><span>X</span><span>{esc(s.get("partner","PARTNER NAME HERE")).upper()}</span></div>'
            f'<div class="rule abs" style="left:{m}px;right:{m}px;top:{92*u}px"></div>')
    name = f'<span class="hl" style="font-size:{34*u}px">{esc(s.get("name","")).upper()}</span>'
    if s.get("short"):
        photo = f'<img class="photo" src="{ph}" style="left:{m}px;right:{m}px;top:{H*0.53}px;width:{W-2*m}px;height:{H*0.4}px;object-position:{s.get("focus","50% 30%")}">' if ph else ""
        return f"""{head}{photo}
<div class="abs" style="left:{m}px;right:{m}px;top:{150*u}px;height:{H*0.37}px">{name}
  <div class="hd fit" data-name="quote" style="font-size:{118*u}px;margin-top:{26*u}px">“{rich(s.get('quote',''))}”</div></div>"""
    photo = f'<img class="photo" src="{ph}" style="left:{W*0.5}px;top:{150*u}px;width:{W*0.42}px;height:{H*0.36}px;object-position:{s.get("focus","50% 35%")}">' if ph else ""
    return f"""{head}{photo}
<div class="abs" style="left:{m}px;right:{m}px;top:{H*0.55}px;height:{H*0.4}px">{name}
  <div class="fit" data-name="quote" style="font:400 calc(var(--u)*38)/1.5 HX;margin-top:{34*u}px">“{rich(s.get('quote',''))}”</div></div>"""


def T_checklist(s, b, W, H, u, m):
    """Two columns: do / don't. p26."""
    def col(title, items, mark, filled):
        st = "background:#fff;color:#000" if filled else "border:calc(var(--u)*1.6) solid #fff"
        li = "".join(f'<div style="margin-top:{14*u}px">{mark}&nbsp;&nbsp;{rich(i)}</div>' for i in items)
        return (f'<div style="flex:1"><span style="{st};display:inline-block;padding:{8*u}px {14*u}px;font:500 calc(var(--u)*24)/1 HX;'
                f'text-transform:uppercase">{esc(title)}</span><div style="font:400 calc(var(--u)*24)/1.3 HX;margin-top:{24*u}px">{li}</div></div>')
    yes = col(s.get("yes_title", "YOU CAN"), s.get("yes", []), "✓", True)
    no = col(s.get("no_title", "PLEASE DON'T"), s.get("no", []), "✕", False)
    return f"""
<div class="abs" style="left:{m}px;right:{m}px;top:{H*0.17}px;height:{H*0.14}px">{hd(s.get('headline',''), s.get('size',76))}</div>
<div class="abs" style="left:{m}px;right:{m}px;top:{H*0.34}px;display:flex;gap:{40*u}px">{yes}{no}</div>
{pill(s)}{sub(s)}"""


def T_list(s, b, W, H, u, m):
    """Numbered list over a photo: 01 … 04. p49 (story 'INSIDE')."""
    ph = image(s.get("photo"), b)
    items = "".join(f'<div style="margin-top:{40*u}px"><span class="hl mono" style="font-size:{30*u}px">{i+1:02d}</span>'
                    f'<div style="font:400 calc(var(--u)*32)/1.2 HX;margin-top:{10*u}px">{rich(t)}</div></div>'
                    for i, t in enumerate(s.get("items", [])))
    return f"""
<img class="photo" src="{ph}" style="inset:0;width:100%;height:100%;object-position:{s.get('focus','30% 40%')}">{dim(.55,'full')}
<div class="abs" style="left:{m}px;right:{m}px;top:{H*0.1}px;height:{H*0.12}px">{hd(s.get('headline','INSIDE'), s.get('size',176))}</div>
<div class="abs" style="left:{W*0.3}px;right:{m}px;top:{H*0.26}px">{items}</div>
{logo(s)}{pill(s, style='top:auto;bottom:calc(var(--u)*90);left:auto;right:var(--m)')}"""


def T_cta(s, b, W, H, u, m):
    """Finisher: centred call to action, pill, subline; optional dimmed photo. p42/p43, p45, p65 (story)."""
    ph = image(s.get("photo"), b)
    bg = (f'<img class="photo" src="{ph}" style="inset:0;width:100%;height:100%;object-position:{s.get("focus","50% 50%")}">' + dim(.55, 'full')) if ph else ""
    return f"""{bg}
<div class="abs" style="left:{m}px;right:{m}px;top:{H*0.3}px;height:{H*0.32}px;display:flex;align-items:center">
  {hd(s.get('headline',''), s.get('size',156), align='center', style='width:100%')}</div>
{('<div class="pill" style="top:'+str(H*0.68)+'px;left:50%;transform:translateX(-50%)">'+esc(s['button'])+'</div>') if s.get('button') else ''}
{logo(s, 'tc') if s.get('logo_top', H > 1600) else logo(s)}{sub(s, 'left:0;right:0;text-align:center' if s.get('center_sub', True) else '')}{pill(s) if s.get('label') else ''}"""


TEMPLATES = {"cover": T_cover, "cover-full": T_cover_full, "cover-sandwich": T_cover_sandwich, "event": T_event,
             "partner": T_partner, "photo-text": T_photo_text, "text": T_text, "subheads": T_subheads,
             "stats": T_stats, "schedule": T_schedule, "quote": T_quote, "checklist": T_checklist,
             "list": T_list, "cta": T_cta}


def build(s, base):
    fmt = s.get("format", "feed")
    W, H = FORMATS[fmt]
    u = W / 1080
    m = 72 * u
    t = s.get("template", "cover")
    if t not in TEMPLATES:
        sys.exit(f"Unknown template '{t}'. Use one of: {', '.join(TEMPLATES)}")
    ground = GROUNDS.get(s.get("ground", "black"), "#000")
    inner = TEMPLATES[t](s, base, W, H, u, m)
    # stories: keep everything inside the IG safe band (top 250 / bottom 340) by insetting the whole layout
    if fmt == "story" and s.get("safe", True):
        inner = f'<div class="abs" style="left:0;right:0;top:{0 if t in ("cover-full","list","cta") else 0}px;bottom:0">{inner}</div>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{esc(t)}</title>
<style>{fonts_css()}{CSS}:root{{--W:{W}px;--H:{H}px;--u:{u}px;--m:{m}px;--ground:{ground}}}</style></head>
<body data-w="{W}" data-h="{H}"><div class="c">{inner}</div>{FIT_JS}</body></html>"""


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    bp = os.path.abspath(sys.argv[1])
    base = os.path.dirname(bp)
    brief = json.load(open(bp))
    slides = brief.get("slides") or [{}]
    top = {k: v for k, v in brief.items() if k != "slides"}
    out = os.path.join(base, brief.get("out", os.path.splitext(os.path.basename(bp))[0]))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    for i, sl in enumerate(slides, 1):
        s = {**top, **sl}
        name = f"{out}-{i}" if len(slides) > 1 else out
        open(name + ".html", "w").write(build(s, base))
        if "--html" in sys.argv:
            print(name + ".html")
            continue
        subprocess.run(["bash", os.path.join(SKILL, "scripts", "render.sh"), name + ".html", name + ".png"], check=True)


if __name__ == "__main__":
    main()
