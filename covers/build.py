#!/usr/bin/env python3
"""Build the Arcane Archives product covers.

Emits, for each cover in COVERS:
  <slug>.html      standalone page, for rendering a PNG
  <Name>.dc.html   the same design as a canvas artboard

    pip install fonttools brotli && python3 covers/build.py

Typefaces are subset to only the characters each cover uses and inlined as
woff2 data URIs. That is deliberate: a linked webfont does not survive PNG
export, and on a poster the type IS the design.
"""

import base64, io, json, re
from pathlib import Path
from fontTools import subset
from fontTools.ttLib import TTFont

HERE = Path(__file__).resolve().parent
FONT_DIR = Path("/mnt/skills/examples/canvas-design/canvas-fonts")

W, H = 800, 1200
INK = "#f2f0f6"          # near-white, faintly warm
DIM = "#8b8794"          # attribute row
SOFT = "#a6a1b0"         # subtitle
BG = "#08070c"

FONTS = {
    "display": FONT_DIR / "BigShoulders-Bold.ttf",
    "meta":    FONT_DIR / "InstrumentSans-Bold.ttf",
    "serif":   FONT_DIR / "CrimsonPro-Regular.ttf",
}

# Stroke-drawn marks on a shared 120-unit grid, one weight, one style.
ICONS = {
    # attraction / union — a vesica, not a figure on a black box
    "vesica": """
      <circle cx="44" cy="60" r="29"/><circle cx="76" cy="60" r="29"/>
      <circle cx="60" cy="60" r="4.5" fill="currentColor" stroke="none"/>""",
    # the primal *code* — a double helix
    # Both strands start and end on the centre line and cross at 47 and 83, so
    # they read as a helix. Rungs sit at the widest separation, never at a
    # crossing -- rungs on the crossings closed the curves into a vase shape.
    "helix": """
      <path d="M60,11 C104,25 104,33 60,47 C16,61 16,69 60,83 C104,97 104,105 60,119"/>
      <path d="M60,11 C16,25 16,33 60,47 C104,61 104,69 60,83 C16,97 16,105 60,119"/>
      <path d="M29,29 H91 M29,65 H91 M29,101 H91"/>""",
    # a peptide chain through a ring
    "chain": """
      <path d="M12,34 L32,20 L52,33 L60,39"/>
      <path d="M60,39 L82.5,52 L82.5,78 L60,91 L37.5,78 L37.5,52 Z"/>
      <path d="M60,91 L68,97 L88,110 L108,96"/>
      <circle cx="12" cy="34" r="4.5" fill="currentColor" stroke="none"/>
      <circle cx="32" cy="20" r="4.5" fill="currentColor" stroke="none"/>
      <circle cx="88" cy="110" r="4.5" fill="currentColor" stroke="none"/>
      <circle cx="108" cy="96" r="4.5" fill="currentColor" stroke="none"/>""",
    # reading people — an eye, ringed
    "eye": """
      <circle cx="60" cy="60" r="54"/>
      <path d="M18,60 C36,38 84,38 102,60 C84,82 36,82 18,60 Z"/>
      <circle cx="60" cy="60" r="13"/>
      <circle cx="60" cy="60" r="4.5" fill="currentColor" stroke="none"/>""",
}

COVERS = [
    dict(slug="arcane-game", name="Main", label="The Arcane Game", accent="#8b5cf6", icon="vesica",
         line1="THE ARCANE", line2="GAME",
         meta="ATTRACTION · SOCIAL DYNAMICS · POWER",
         sub="The unfiltered manual on modern attraction"),
    dict(slug="primal-code", name="PrimalCode", label="The Primal Code", accent="#2fd671", icon="helix",
         line1="THE PRIMAL", line2="CODE",
         meta="HEALTH · BIOHACKING · ASCENDANCE",
         sub="Build a body that opens doors before you speak"),
    dict(slug="peptides-101", name="Peptides101", label="Peptides 101", accent="#3b95f0", icon="chain",
         line1="PEPTIDES", line2="101",
         meta="BIOHACKING · PERFORMANCE · LONGEVITY",
         sub="The science of engineered optimization"),
    dict(slug="dark-psych-codex", name="DarkPsychCodex", label="The Dark Psych Codex", accent="#f04444", icon="eye",
         line1="THE DARK", line2="PSYCH CODEX", size=130,
         meta="INFLUENCE · PERSUASION · PROTECTION",
         sub="The psychology they don't teach in school"),
]

LOCKUP = "ARCANE ARCHIVES"
DOMAIN = "ARCANEARCHIVES.SHOP"

MARK = ('<svg viewBox="239 204 547 570" fill="currentColor" aria-hidden="true">'
        '<g transform="translate(0,1024) scale(0.1,-0.1)"><path d="'
        + re.sub(r"\s+", " ", (HERE.parent / "brand/arcane-mark.svg").read_text()
                 .split('<path d="')[1].split('"')[0]).strip()
        + '"/></g></svg>')


def woff2(path: Path, chars: str) -> str:
    """Subset `path` down to `chars` and return it as a bare base64 woff2."""
    font = TTFont(str(path))
    opts = subset.Options()
    opts.layout_features = ["kern", "liga", "calt"]
    opts.notdef_outline = True
    opts.desubroutinize = True
    s = subset.Subsetter(options=opts)
    s.populate(text=chars)
    s.subset(font)
    font.flavor = "woff2"
    buf = io.BytesIO()
    font.save(buf)
    return base64.b64encode(buf.getvalue()).decode()


def face(family: str, b64: str) -> str:
    return (f"@font-face{{font-family:'{family}';font-weight:400;font-style:normal;"
            f"font-display:block;src:url(data:font/woff2;base64,{b64}) format('woff2');}}")


def body(c: dict, accent: str) -> str:
    """The cover markup. `accent` is a literal hex or a {{hole}}."""
    return f"""
<div style="position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{BG};">

  <div style="position:absolute;left:50%;top:430px;width:1120px;height:1120px;
              transform:translate(-50%,-50%);pointer-events:none;opacity:.19;
              background:radial-gradient(circle closest-side,{accent} 0%,transparent 72%);"></div>

  <div style="position:absolute;left:0;right:0;bottom:0;height:440px;pointer-events:none;
              opacity:.14;background:linear-gradient(to top,{accent} 0%,transparent 100%);"></div>

  <div style="position:relative;display:flex;flex-direction:column;align-items:center;
              padding:150px 64px 0;">

    <div style="color:{accent};width:206px;height:206px;margin-bottom:66px;">
      <svg viewBox="0 0 120 130" width="206" height="206" fill="none" stroke="currentColor"
           stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">{ICONS[c['icon']]}</svg>
    </div>

    <div style="font-family:'ArcaneDisplay',Impact,'Haettenschweiler','Arial Narrow',sans-serif;
                font-size:{c.get('size', 142)}px;line-height:.84;letter-spacing:.006em;
                text-align:center;white-space:nowrap;">
      <div style="color:{INK};">{c['line1']}</div>
      <div style="color:{accent};">{c['line2']}</div>
    </div>

    <div style="font-family:'ArcaneMeta','Helvetica Neue',Arial,sans-serif;font-size:19px;
                letter-spacing:.235em;color:{DIM};margin-top:46px;text-align:center;">{c['meta']}</div>

    <div style="width:104px;height:2px;background:{accent};margin-top:30px;opacity:.9;"></div>

    <div style="font-family:'ArcaneSerif',Georgia,'Times New Roman',serif;font-size:29px;
                color:{SOFT};margin-top:32px;text-align:center;text-wrap:pretty;">{c['sub']}</div>
  </div>

  <div style="position:absolute;left:64px;right:64px;bottom:58px;display:flex;
              flex-direction:column;align-items:center;">
    <div style="width:100%;height:1px;background:rgba(255,255,255,.09);margin-bottom:34px;"></div>
    <div style="width:44px;height:44px;color:{INK};margin-bottom:12px;">{MARK}</div>
    <div style="font-family:'ArcaneSerif',Georgia,'Times New Roman',serif;font-size:21px;
                letter-spacing:.34em;color:{INK};text-indent:.34em;">{LOCKUP}</div>
    <div style="font-family:'ArcaneMeta','Helvetica Neue',Arial,sans-serif;font-size:11px;
                letter-spacing:.28em;color:{DIM};margin-top:14px;text-indent:.28em;">{DOMAIN}</div>
  </div>
</div>"""


def build():
    for c in COVERS:
        used = "".join({*(c["line1"] + c["line2"] + c["meta"] + c["sub"]
                          + LOCKUP + DOMAIN + "0123456789")})
        faces = "".join([
            face("ArcaneDisplay", woff2(FONTS["display"], c["line1"] + c["line2"])),
            face("ArcaneMeta", woff2(FONTS["meta"], c["meta"] + DOMAIN)),
            face("ArcaneSerif", woff2(FONTS["serif"], c["sub"] + LOCKUP)),
        ])
        css = faces + "html,body{margin:0;background:" + BG + ";}"

        (HERE / f"{c['slug']}.html").write_text(
            f"<!doctype html><html><head><meta charset=utf-8><title>{c['line1']} {c['line2']}"
            f"</title><style>{css}</style></head><body>{body(c, c['accent'])}</body></html>")

        props = ('{"accent":{"editor":"color","default":"' + c["accent"] + '"},'
                 '"$preview":{"width":' + str(W) + ',"height":' + str(H) + '}}')
        (HERE / f"{c['name']}.dc.html").write_text(
            "<!doctype html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n"
            "<script src=\"./support.js\"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n"
            f"<style>{css}a{{color:{c['accent']};}}a:hover{{color:{INK};}}</style>\n</helmet>\n"
            + body(c, "{{accent}}")
            + "\n</x-dc>\n<script data-dc-script data-props='" + props + "'>\n"
            "class Component extends DCLogic {\n"
            f"  renderVals() {{ return {{ accent: this.props.accent ?? '{c['accent']}' }}; }}\n"
            "}\n</script>\n</body>\n</html>\n")
        print(f"  {c['slug']}.html + {c['name']}.dc.html")

    # One row of frames, 80px of clear space between each.
    boards = [{"file": f"{c['name']}.dc.html", "title": c["label"],
               "x": i * (W + 80), "y": 0, "w": W, "h": H}
              for i, c in enumerate(COVERS)]
    (HERE / "canvas.json").write_text(json.dumps(
        {"artboards": boards, "launch": {"view": "canvas"}}, indent=2) + "\n")

    print("built", len(COVERS), "covers + canvas.json")


if __name__ == "__main__":
    build()
