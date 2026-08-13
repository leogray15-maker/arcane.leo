# Leo Gray | Arcane — link hub

A Linktree replacement, built as one self-contained `index.html`. No build step,
no dependencies, no monthly fee, no Linktree branding — and unlike Linktree it
can show social proof, rank links by importance, and carry your own visual
identity.

## Add your real logo (one upload, no code change)

The mark currently on the page is **hand-traced by eye** from the logo images —
close, but not the real artwork. To use the genuine file:

1. Take the **white** version of the logo (`.svg` preferred — it stays sharp at
   any size; `.png` also works).
2. Rename it exactly **`arcane-logo.svg`**.
3. Upload it into this repo next to `index.html`. On github.com: open the repo,
   switch to this branch, then **Add file → Upload files**.

That's it. The page detects the file and uses it for both the avatar and the
browser-tab icon automatically. If the file isn't there, it silently falls back
to the trace, so the page never breaks either way.

Using a different name or extension? Change `LOGO` at the bottom of
`index.html` to match.

## What still needs filling in

| Item | Where | Status |
| --- | --- | --- |
| Real logo file | upload as `arcane-logo.svg` | traced fallback in use |
| Arcane Healing Protocols URL | `LINKS` array | renders as **Soon** until set |
| WhatsApp number | `LINKS` array | renders as **Soon** until set |
| Profile photo | `AVATAR` const | falls back to the logo |

For WhatsApp, the URL format is `https://wa.me/<number>` — country code
included, no `+`, no spaces. A UK mobile `07700 900123` becomes
`https://wa.me/447700900123`.

## Current links

| Entry | Destination |
| --- | --- |
| The Arcane Archives | https://arcanearchives.shop |
| Arcane Healing Protocols | *(needs URL)* |
| Arcane Track | https://arcanetrack.vercel.app |
| Arcane Peptides | https://arcanepeptides.vercel.app |
| WhatsApp me | *(needs number)* |
| Instagram | https://instagram.com/arcaneleo.g |
| TikTok | https://tiktok.com/@arcane_advice |

## Editing

Everything editable sits in one block near the bottom of `index.html`, marked
`EDIT HERE`: `AVATAR`, `PROOF`, `LINKS`, `QUOTE`, and `SOCIALS`.

Each entry in `LINKS` takes:

- **`url`** — the destination. Set it to `"#"` and the card renders dimmed with
  a **Soon** badge and isn't clickable.
- **`title` / `sub`** — the label and the grey line under it. `sub` wraps to two
  lines, so moderately long copy is fine.
- **`icon`** — `book`, `list`, `spark`, `flask`, `whatsapp`, `instagram`,
  `tiktok`, or `link`. Unknown values fall back to `link`.
- **`badge`** — optional violet pill, e.g. `"Free"`, `"New"`, `"20% off"`.
- **`featured: true`** — renders as the hero card: bigger, gradient-filled,
  glowing. Use it on exactly one entry; its pull comes from being the only one.
- **`style: "chat"`** — the green WhatsApp treatment.

Reorder the array to reorder the page. The markup is generated from it, so you
never touch HTML.

## Why it's laid out this way

- **The first card takes a disproportionate share of clicks**, so Archives is
  featured and sits first. Move a different entry to the top if the priority
  changes.
- **Arcane Track is badged Free** — it's the cheapest yes for someone arriving
  cold from TikTok, and it makes the paid links feel less like the only ask.
- **WhatsApp sits last, styled differently.** It's the catch for people who
  read everything and still want to talk before buying — the highest-intent
  visitors you have.
- **The testimonial sits below the links, not above.** It answers the doubt
  that surfaces *after* someone considers buying, which is where proof does the
  most work.

## The testimonial

`QUOTE` currently holds a message from your TikTok content. Set `QUOTE = null`
to hide the section. Two things worth doing:

- Confirm the sender is fine with it being quoted on a public page, even
  unattributed.
- Keep the attribution vague ("a follower") rather than inventing a name.

## Deploying

Fully static — any host works. **Vercel** is consistent with your other two
sites: import the repo, leave the build command empty, publish directory is the
repo root. **GitHub Pages:** Settings → Pages → deploy from branch, `/ (root)`.

Once it's live, swap the `linktr.ee/Arcaneleo.g` link in your TikTok bio and the
`arcanearchives.shop` link in your Instagram bio for the new URL.

## Notes

- Palette is violet to match the Archives and Track logos — `--violet`,
  `--violet-lo`, `--violet-hi` in `:root`.
- The inline traced mark is a fallback only. See "Add your real logo" above to
  replace it with the genuine artwork.
- Add an `og:image` (1200×630) when you have artwork; it controls the preview
  card when the link is shared.
- The footer disclaimer covers educational-use, research-use, and
  individual-results. Given the health claims in this niche and the existing
  TikTok account warning, keep it.
