# Product covers

Ten products, generated from `build.py` so the whole set stays consistent —
change one thing in `COVERS` and everything rebuilds.

```
pip install fonttools brotli
python3 covers/build.py
```

Each product emits four files: `<slug>.html` and `<slug>-banner.html` (the
standalone pages the PNGs are rendered from), plus `<Name>.dc.html` and
`<Name>Banner.dc.html` (the same two designs as canvas artboards). `canvas.json`
puts the covers on one canvas page and the banners on another.

The banner is **not a crop of the cover**. A 2:3 portrait sliced to 10:3 loses
the mark and most of the title, so the banner is laid out for its own shape:
mark left, title and attributes right. Everything else — palette, typefaces,
the kiss on The Arcane Game — is shared, so the two read as the same product.

`thumb/*.webp` are the banners at 1080px wide, which is what the link hub
loads. They are sized for the small end: the hub renders them at roughly a
third of that, so the attribute row and the corner mark are deliberately
larger than full-scale composition would want.

## What each cover carries

| Field | What it is |
| --- | --- |
| `accent` | the one colour that separates this product from the others |
| `icon` | a key into `ICONS` — `woman`, `helix`, `chain`, `eye`, `vesica` |
| `icon_size` | icon height in px, default 206 — a standing figure is narrow, so it needs more |
| `kiss` | stamps the lipstick print across the title |
| `line1` / `line2` | the title; line 2 takes the accent colour |
| `meta` | the three-part attribute row |
| `sub` | the one-line promise under the rule |
| `size` | title size, only where the default 142 doesn't fit |

## Why it looks like this

- **Titles never wrap.** `white-space: nowrap` plus a per-cover `size`. Letting
  a title wrap turned The Dark Psych Codex into a three-line cover while the
  other three were two-line, and it stopped looking like a set.
- **Typefaces are subset and inlined as woff2 data URIs.** A linked webfont
  does not survive PNG export, and on a poster the type is the design. Each
  cover carries only the characters it actually uses, so the whole file is
  ~13 KB rather than ~400 KB.
- **The marks are drawn on one 120-unit grid at one stroke weight.** The old
  set mixed a raster illustration with vector glyphs at different weights, so
  the four never read as a family.
- **The Arcane Game keeps its figure and its kiss** — they were the point, not
  a mistake. Both are vector now, so the gown sits on the cover background
  instead of on its own black square, and the kiss lands across a letter of
  THE ARCANE, which is long enough to still read. It will not go on GAME: at
  four letters, a kiss big enough to see leaves "GAM".
- **Red on this cover is deliberate, not the accent.** `LIP` drives the gown
  and the kiss; the accent still drives the title, rule and glow. It is the one
  cover in the set using two colours.
- **The footer is anchored and the lower half carries a wash.** The old covers
  put everything in the top 55% and left the bottom empty. A rule, a bigger
  lockup and a soft accent gradient give the bottom something to be.

## Regenerating the PNGs

`build.py` writes HTML, not images. Open a `<slug>.html` at 800x1200 and
screenshot the outer `div` at 2x for a 1600x2400 PNG — or open the canvas and
use its PNG export.

## Naming

**The Quiet Empire** and **The Inner Citadel** are proposed names, not given
ones — the source PDFs never arrived, so both were named from a description of
their contents ("productive isolation / entrepreneurship mastery" and "mindset
mastery / mind hijacking"). Renaming either is one line in `COVERS`; the
artwork follows.

## Accent hues

Spread around the wheel so no two cards adjacent in a hub section read as the
same product: 0 red, 25 orange, 45 gold, 80 lime, 145 green, 185 cyan, 210
blue, 233 indigo, 263 violet, 340 rose. Adding an eleventh product means
finding a gap, not picking a colour you like.

## Not on the hub yet

**The Primal Code**, **The Quiet Empire** and **The Inner Citadel** have
artwork but no URL, so they are built but not linked.
