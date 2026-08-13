# Arcane Leo — link hub

A single-page link hub: Arcane Archives (education), Arcane Track, Arcane
Peptides, and socials. Built as one self-contained `index.html` — no build
step, no dependencies, no framework.

## Current links

| Entry | Destination |
| --- | --- |
| Arcane Archives | https://arcanearchives.shop |
| Arcane Track | https://arcanetrack.vercel.app |
| Arcane Peptides | https://arcanepeptides.vercel.app |
| Instagram | https://instagram.com/arcaneleo.g |
| TikTok | https://tiktok.com/@arcane_advice |

## Editing the links

Everything you need to change lives in two arrays near the bottom of
`index.html`, under the `EDIT HERE` comment:

```js
const LINKS = [
  { title: "Arcane Track", sub: "See what's actually working",
    url: "https://arcanetrack.vercel.app", icon: "spark", badge: "Free" },
  ...
];

const SOCIALS = [
  { title: "Instagram", sub: "@arcaneleo.g",
    url: "https://instagram.com/arcaneleo.g", icon: "instagram" },
  ...
];
```

- **`url`** — the destination. Set it to `"#"` and the entry renders dimmed
  with a **Soon** badge and isn't clickable — useful for announcing something
  before it launches.
- **`title` / `sub`** — the label and the small grey line under it. The `sub`
  wraps to a second line if needed, so longer copy is fine.
- **`icon`** — one of `book`, `spark`, `flask`, `instagram`, `tiktok`, `mail`,
  `link`. Anything unrecognized falls back to `link`.
- **`badge`** — optional gold pill on the right, e.g. `"Free"`, `"New"`,
  `"20% off"`. Omit the field for no badge. Keep it to one or two badges across
  the page — the pull comes from being the exception.

Reorder the arrays to reorder the page. Add or remove entries freely — the list
is generated from the array, so the markup never needs touching.

`http`/`https` links open in a new tab; `mailto:` links don't.

## Ordering, and why it's set this way

The first link takes a large share of all clicks, so the order is a real lever.
Right now it runs Archives → Track (free) → Peptides: the flagship first, then
a free tool that costs a cold visitor nothing to try, then the shop. If you'd
rather push peptide sales directly, move that entry to the top of `LINKS`.

## Adding a new icon

Add an entry to the `ICONS` object with a 24×24 SVG that uses
`stroke="currentColor"` so it picks up the gold accent automatically.

## Deploying

The page is fully static — any host works.

**GitHub Pages:** Settings → Pages → Source: `Deploy from a branch`, pick the
branch and `/ (root)`.

**Netlify / Vercel / Cloudflare Pages:** point at the repo, leave the build
command empty, set the publish directory to the repo root.

## Customizing the look

Colors, spacing, and the max content width are CSS variables in the `:root`
block at the top of the file. `--gold` is the accent used across icons, hover
borders, and focus rings.

## Notes

- The page title is **Arcane Leo** — the umbrella brand — so that "Arcane
  Archives" stays the name of the education platform rather than the hub. Both
  the `<h1>` and the `<title>`/`og:title` tags need changing together if you
  rename it.
- The footer carries an "educational content only / not medical advice"
  disclaimer. Given the peptides and skin-protocol content, keep it.
- Update the `og:` meta tags in `<head>` before sharing the link anywhere —
  they control the preview card on socials. Add an `og:image` (1200×630) when
  you have artwork.
