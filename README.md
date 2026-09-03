# Leo Gray | Arcane — link hub

A Linktree replacement, built as one self-contained `index.html`. No build step,
no dependencies, no monthly fee, no Linktree branding — and unlike Linktree it
can show social proof, rank links by importance, and carry your own visual
identity.

## Brand assets

`brand/` holds the logo artwork:

| File | What it is |
| --- | --- |
| `arcane-mark.svg` | the mark as clean vector — traced from `arcane-mark-black.png` |
| `arcane-mark-black.png` | plain mark, black |
| `arcane-mark-white.png` | plain mark, white |
| `arcane-archives-black.png` | Archives lockup (mark + wordmark), black |
| `arcane-archives-white.png` | Archives lockup, white |
| `arcane-track-icon.png` | Arcane Track app icon |
| `og-image.png` | 1200x630 share card — what WhatsApp/iMessage/X show |

The page doesn't load any of these at runtime — the mark is inlined as SVG in
`index.html` (in `ICONS.mark` and the favicon), so it costs no network request,
stays sharp at every size, and picks up the violet accent automatically. The
files are here as the source of truth for anything else you make.

The one exception is the banner art under `covers/thumb/`, which the three
product cards do load. They are 10-15 KB each, lazy-loaded, and carry explicit
dimensions so nothing shifts as they arrive — cheap enough that showing the
real product beats keeping the page asset-free.

The vector was produced by thresholding the black PNG and tracing it, then
checked against the original: it differs by 0.5% of the mark's area, all of it
edge antialiasing. If you ever get the original vector from your designer, drop
it in and I'll swap it for a byte-exact one.

`og-image.png` is generated, not hand-drawn — `brand/make-og-image.py` rebuilds
it (`pip install Pillow && python3 brand/make-og-image.py`). Edit the script if
the tagline or wordmark changes; committing the regenerated PNG is what ships.

## What still needs filling in

| Item | Where | Status |
| --- | --- | --- |
| Profile photo | `AVATAR` const | falls back to the Arcane mark |
| Prices on the four paid cards | `badge` in `LINKS` | only Archives has one, and it says "Membership" rather than a number |

Every link is live; nothing renders as **Soon**.

### Two different Healing Protocols links

The page points at `buy.stripe.com/8x2aEW7qc9x82wW1260Ba04`. Your Linktree
points the same product at `buy.stripe.com/dRm6oGfWlaBc9Zo4ei0Ba03`. Both are
live Stripe links, so one of them is probably an old price or an old product —
work out which is current and make both places agree. The page was left on the
one it already had rather than silently switching where your money lands.

### Prices

Four cards go straight to Stripe checkout. Cold traffic that lands on a payment
form without knowing the number bounces, and it's the cheapest fix on the page:
put the amount in each card's `badge`, e.g. `badge: "£49"`. The badge renders as
a violet pill on the right of the card (and as an eyebrow above the title on the
featured card).

### WhatsApp link

`https://wa.me/447405557399?text=<prefilled message>` — the number is in
international form (leading `0` dropped, `44` prefixed), which is what `wa.me`
requires. The `?text=` part prefills the first message so nobody has to work
out what to say; edit that string in `LINKS` to change it.

WhatsApp usernames exist but the `wa.me/<username>` form isn't reliably live
for everyone yet, so the number is used here because it works on every device
today. Once your username resolves, switching to it is a one-line change and
has a real advantage: it stops publishing your mobile number on a public page.

## Current links

Cards for The Arcane Game, Deep & Dark Psychology and Peptides 101 are banner
cards carrying their own artwork — see `covers/`. The Primal Code has artwork
but no link yet, so it isn't listed.

| Group | Entry | Destination |
| --- | --- | --- |
| Start here | The Arcane Archives | https://arcanearchives.shop |
| Skin & healing | Arcane Healing Protocols | Stripe (`8x2aEW7qc9x82wW1260Ba04`) |
| Skin & healing | Peptides 101 | Stripe (`5kQ00i39WaBc5J85im0Ba05`) |
| Skin & healing | Arcane Track | https://arcanetrack.vercel.app |
| Skin & healing | Arcane Peptides | https://arcanepeptides.vercel.app |
| Mind & game | Deep & Dark Psychology | Stripe (`7sYfZgh0MfVw2wW8uy0Ba07`) |
| Mind & game | The Arcane Game | Stripe (`5kQeVc25SdNofjl1260Ba06`) |
| Talk to me | WhatsApp me | `wa.me/447405557399` with a prefilled message |
| — | Instagram | https://instagram.com/arcaneleo.g |
| — | TikTok | https://tiktok.com/@arcane_advice |

Peptides 101 is listed on Linktree as "Pept!des 101" — the `!` is there to dodge
platform keyword filters. On your own domain nothing is filtering you, so it's
spelled properly here.

## Editing

Everything editable sits in one block near the bottom of `index.html`, marked
`EDIT HERE`: `AVATAR`, `PROOF`, `LINKS`, `QUOTE`, and `SOCIALS`.

`LINKS` is one flat list that renders top to bottom exactly as written. An
entry of the form `{ section: "Skin & healing" }` starts a new labelled group;
everything after it belongs to that group until the next `section` entry. Add,
rename, or delete a group by editing one line.

Every other entry is a link card, and takes:

- **`url`** — the destination. Set it to `"#"` and the card renders dimmed with
  a **Soon** badge and isn't clickable.
- **`title` / `sub`** — the label and the grey line under it. `sub` wraps to two
  lines, so moderately long copy is fine.
- **`banner`** — path to banner art, e.g. `"covers/thumb/arcane-game.webp"`.
  Turns the row into a banner card: artwork across the full width with a strip
  underneath carrying `sub` and the arrow. The artwork already contains the
  product name, so no title row is drawn — `title` becomes the image's alt
  text and the link's accessible name. Use it on anything with real artwork.
- **`icon`** — `book`, `list`, `spark`, `flask`, `molecule`, `eye`, `target`,
  `whatsapp`, `instagram`, `tiktok`, or `link`. Unknown values fall back to
  `link`. Ignored when `cover` is set.
- **`badge`** — optional violet pill, e.g. `"Free"`, `"£49"`, `"20% off"`. On
  the featured card it renders above the title instead of beside it.
- **`featured: true`** — renders as the hero card: bigger, gradient-filled,
  glowing. Use it on exactly one entry; its pull comes from being the only one.
- **`style: "chat"`** — the green WhatsApp treatment.

Reorder the array to reorder the page. The markup is generated from it, so you
never touch HTML.

## Why it's laid out this way

- **Eight links in one flat column read as a wall** and nobody finishes it. They
  are chunked into four labelled groups — *Start here*, *Skin & healing*,
  *Mind & game*, *Talk to me* — so a visitor scans four short lists instead of
  one long one and can skip straight to the half they came for. No group holds
  more than four entries; that's the point, and it's worth resisting the urge to
  let one grow past five.
- **The two halves of the brand are separated on purpose.** Someone arriving
  from an eczema video and someone arriving from a psychology video want
  completely different things, and mixing peptide protocols with attraction and
  social dynamics in one undifferentiated list makes both look unserious.
- **The first card takes a disproportionate share of clicks**, so Archives is
  featured and sits first. It's also the only recurring-revenue product and the
  one your Linktree data shows winning by a wide margin (66 clicks against 27
  for the runner-up). Move a different entry to the top if the priority changes.
- **Skin & healing sits above Mind & game** because it's the proven inbound —
  it's what the testimonial is about and where the click data is.
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
- The mark in the page is the real logo, vectorised. See "Brand assets" above.
- `og:image`, `og:url` and the canonical link all point at
  `https://arcane-leo.vercel.app/`. If you put the hub on a custom domain,
  those three absolute URLs in `<head>` are the only things that need changing —
  they have to be absolute, so a relative path won't work.
- Cards fade up in sequence on load, 45ms apart. It's disabled outright under
  `prefers-reduced-motion`.
- The footer disclaimer covers educational-use, research-use, and
  individual-results. Given the health claims in this niche and the existing
  TikTok account warning, keep it.
