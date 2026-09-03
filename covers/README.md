# Product covers

Four cover posters, generated from `build.py` so the whole set stays
consistent — change one thing in `COVERS` and all four rebuild.

```
pip install fonttools brotli
python3 covers/build.py
```

Each cover emits twice: `<slug>.html` (a standalone page, what the PNGs are
rendered from) and `<Name>.dc.html` (the same design as a canvas artboard).
`canvas.json` lays the four out in a row.

## What each cover carries

| Field | What it is |
| --- | --- |
| `accent` | the one colour that separates this product from the others |
| `icon` | a key into `ICONS` — `vesica`, `helix`, `chain`, `eye` |
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
- **The footer is anchored and the lower half carries a wash.** The old covers
  put everything in the top 55% and left the bottom empty. A rule, a bigger
  lockup and a soft accent gradient give the bottom something to be.

## Regenerating the PNGs

`build.py` writes HTML, not images. Open a `<slug>.html` at 800x1200 and
screenshot the outer `div` at 2x for a 1600x2400 PNG — or open the canvas and
use its PNG export.

## Not covered yet

There is no cover for **Arcane Healing Protocols**, which is the second
best-selling product on the Linktree. Adding one is a new entry in `COVERS`.
