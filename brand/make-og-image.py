#!/usr/bin/env python3
"""Regenerate brand/og-image.png — the 1200x630 card that platforms show when
the hub link is shared (WhatsApp, iMessage, Instagram DM, X, Facebook).

    pip install Pillow && python3 brand/make-og-image.py

Fonts: Outfit (SIL Open Font License). Point FONT_DIR at any copy of it, or
swap in another face — only the two paths below need to change.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
FONT_DIR = Path("/mnt/skills/examples/canvas-design/canvas-fonts")
BOLD = FONT_DIR / "Outfit-Bold.ttf"
REG = FONT_DIR / "Outfit-Regular.ttf"

W, H = 1200, 630
BG = (8, 7, 13)
VIOLET_HI = (167, 139, 250)
TEXT = (244, 242, 248)
MUTED = (155, 150, 172)

# (centre x, centre y, radius, rgb, peak opacity) — same three washes as the page
GLOWS = [
    (600, 10, 660, (109, 77, 240), 0.34),
    (1160, 660, 520, (76, 60, 160), 0.30),
    (90, 300, 420, (139, 92, 246), 0.13),
]


def glow_layer(cx, cy, r, rgb, peak, scale=8):
    """A soft radial wash, rendered small and scaled up so it stays smooth."""
    w, h = W // scale, H // scale
    mask = Image.new("L", (w, h), 0)
    px = mask.load()
    for y in range(h):
        dy = y * scale - cy
        for x in range(w):
            dx = x * scale - cx
            d = (dx * dx + dy * dy) ** 0.5
            if d < r:
                t = 1.0 - d / r
                px[x, y] = int(255 * peak * t * t)
    mask = mask.resize((W, H), Image.BICUBIC)
    layer = Image.new("RGBA", (W, H), rgb + (0,))
    layer.putalpha(mask)
    return layer


def build():
    img = Image.new("RGBA", (W, H), BG + (255,))
    for cx, cy, r, rgb, peak in GLOWS:
        img.alpha_composite(glow_layer(cx, cy, r, rgb, peak))

    # --- the mark, recoloured from the white artwork's alpha ---
    src = Image.open(HERE / "arcane-mark-white.png").convert("RGBA")
    size = 250
    alpha = src.getchannel("A").resize((size, size), Image.LANCZOS)
    mark = Image.new("RGBA", (size, size), VIOLET_HI + (0,))
    mark.putalpha(alpha)

    mx, my = 138, (H - size) // 2
    # a halo so the mark doesn't sit flat on the background
    halo = glow_layer(mx + size // 2, my + size // 2, 260, (139, 92, 246), 0.45)
    img.alpha_composite(halo)
    img.alpha_composite(mark, (mx, my))

    d = ImageDraw.Draw(img)
    f_name = ImageFont.truetype(str(BOLD), 76)
    f_tag = ImageFont.truetype(str(REG), 40)
    f_foot = ImageFont.truetype(str(REG), 27)

    x = mx + size + 74
    y = 196

    # "Leo Gray | Arcane" — the pipe picks up the accent, as it does on the page
    for part, font, fill in (("Leo Gray", f_name, TEXT),
                             (" | ", f_name, VIOLET_HI),
                             ("Arcane", f_name, TEXT)):
        d.text((x, y), part, font=font, fill=fill)
        x += d.textlength(part, font=font)

    y += 104
    for line in ("The Knowledge They Don't", "Want You To Know"):
        d.text((mx + size + 74, y), line, font=f_tag, fill=(207, 198, 234))
        y += 52

    d.text((mx + size + 74, y + 22),
           "Protocols  ·  Peptides  ·  Psychology  ·  Trading",
           font=f_foot, fill=MUTED)

    out = HERE / "og-image.png"
    img.convert("RGB").save(out, "PNG", optimize=True)
    print(f"wrote {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    build()
