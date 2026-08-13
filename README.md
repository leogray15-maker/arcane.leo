# Arcane Archives — link hub

A single-page link hub for Arcane Archives: the education platform, the skin
healing tracker, Arcane Peptides, and socials. Built as one self-contained
`index.html` — no build step, no dependencies, no framework.

## Editing the links

Everything you need to change lives in two arrays near the bottom of
`index.html`, under the `EDIT HERE` comment:

```js
const LINKS = [
  { title: "Arcane Archives", sub: "Education platform...", url: "#", icon: "book" },
  ...
];

const SOCIALS = [
  { title: "Instagram", sub: "@arcane.archives", url: "#", icon: "instagram" },
  ...
];
```

- **`url`** — the destination. Leave it as `"#"` and the entry renders dimmed
  with a **Soon** badge and isn't clickable, so you can publish the page before
  every product is live.
- **`title` / `sub`** — the label and the small grey line under it.
- **`icon`** — one of `book`, `spark`, `flask`, `instagram`, `tiktok`, `mail`,
  `link`. Anything unrecognized falls back to `link`.

Reorder the arrays to reorder the page. Add or remove entries freely — the list
is generated from the array, so the markup never needs touching.

`http`/`https` links open in a new tab; `mailto:` links don't.

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

- The footer carries an "educational content only / not medical advice"
  disclaimer. Given the peptides and skin-protocol content, keep it.
- Update the `og:` meta tags in `<head>` before sharing the link anywhere —
  they control the preview card on socials. Add an `og:image` (1200×630) when
  you have artwork.
