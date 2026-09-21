# Leo Gray | Arcane — link hub

A landing page, built as one self-contained `index.html`. No build step, no
dependencies, no monthly fee, no Linktree branding.

It is **three offers stacked in order of how much you want them taken**, not a
list of links:

1. **The Arcane Archives** — the membership. Above the fold, biggest, brightest,
   full-width button. Six individual products live inside a collapsed expander
   beneath it so they never compete with the membership.
2. **Arcane Peptides** — the shop. Flat card, its own orange, research-use line
   under its own button.
3. **Arcane Track** — the tracker, £11.99/mo or £70/year. Flat card, its own
   green, and the healing testimonial directly underneath it.

The previous version was eight product cards of roughly equal weight in one
scroll. Eight equal choices is not a menu, it is a decision to postpone, and the
membership — the only recurring revenue on the page — was one card among eight.
That is the problem this layout exists to fix.

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

The banner art under `covers/thumb/` is no longer loaded at runtime. The page
used to render every product as a banner card; it now renders three hero
sections and six compact rows, each carrying its product's glyph lifted from
that product's cover art rather than the full artwork. The `.webp` files are
kept because the covers are still the source of truth for each product's
colour and mark — and because putting a banner back is a one-line change if
you want one.

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
| The Inner Citadel link | `ARCHIVES.items` | `url: "#"` — renders dimmed with a **Soon** badge |
| The Primal Code link | `ARCHIVES.items` | `url: "#"` — renders dimmed with a **Soon** badge |

**The Quiet Empire has no row**, and that is a decision rather than an
oversight — the six products specified for the expander didn't include it. Its
artwork and its colour (`#6d7cf8`) are still in `covers/`, so adding a seventh
row is a six-line paste into `ARCHIVES.items` whenever the seventh product is
ready. Nothing in Hero 1's copy counts the products any more, so a seventh row
needs no copy change to go with it.

**There is no free entry point on the page any more.** Track used to be the
cheapest yes — the thing someone arriving cold from TikTok could take without
deciding anything. The cheapest yes is now £11.99/mo. If the funnel wants a
free step back, it has to come from somewhere else: a free tier of Track, a
lead magnet, or a free module out of the Archives.

### Two different Healing Protocols links

The page points at `buy.stripe.com/8x2aEW7qc9x82wW1260Ba04`. Your Linktree
points the same product at `buy.stripe.com/dRm6oGfWlaBc9Zo4ei0Ba03`. Both are
live Stripe links, so one of them is probably an old price or an old product —
work out which is current and make both places agree. The page was left on the
one it already had rather than silently switching where your money lands.

### Prices

Every button on the page carries its own number: `Join The Archives — £128/mo`,
`Shop Peptides`, and `Get Arcane Track — £11.99/mo` with the £70 annual price
in the `fineprint` line under it. Cold traffic that lands on a payment form
without knowing the number bounces, which is why the price is on the button
rather than one click later.

The four expander rows that go straight to Stripe still don't show a number.
That is a deliberate trade for now: a price on every row turns the expander back
into a comparison table, which is the decision paralysis this layout removes.
If you want them, the place to put one is the end of each row's `sub`.

### WhatsApp link

`https://wa.me/447405557399?text=<prefilled message>` — the number is in
international form (leading `0` dropped, `44` prefixed), which is what `wa.me`
requires. The `?text=` part prefills the first message so nobody has to work
out what to say; edit that string in `TALK` to change it.

WhatsApp usernames exist but the `wa.me/<username>` form isn't reliably live
for everyone yet, so the number is used here because it works on every device
today. Once your username resolves, switching to it is a one-line change and
has a real advantage: it stops publishing your mobile number on a public page.

## Where everything points

| Section | Entry | Destination |
| --- | --- | --- |
| Hero 1 | Join The Archives — £128/mo | https://arcanearchives.shop |
| Hero 1 expander | The Dark Psych Codex | Stripe (`7sYfZgh0MfVw2wW8uy0Ba07`) |
| Hero 1 expander | The Arcane Game | Stripe (`5kQeVc25SdNofjl1260Ba06`) |
| Hero 1 expander | The Inner Citadel | **no link yet** — renders as Soon |
| Hero 1 expander | The Primal Code | **no link yet** — renders as Soon |
| Hero 1 expander | Healing Protocols | Stripe (`8x2aEW7qc9x82wW1260Ba04`) |
| Hero 1 expander | Peptides 101 | Stripe (`5kQ00i39WaBc5J85im0Ba05`) |
| Hero 2 | Shop Peptides | https://arcanepeptides.vercel.app |
| Hero 3 | Get Arcane Track — £11.99/mo | https://arcanetrack.vercel.app |
| Talk to me | WhatsApp me | `wa.me/447405557399` with a prefilled message |
| Follow | Instagram | https://instagram.com/arcaneleo.g |
| Follow | TikTok | https://tiktok.com/@arcane_advice |

Peptides 101 is listed on Linktree as "Pept!des 101" — the `!` is there to dodge
platform keyword filters. On your own domain nothing is filtering you, so it's
spelled properly here.

## Editing

Everything editable sits in one block near the bottom of `index.html`, marked
`EDIT HERE`: `AVATAR`, `PROOF`, `ARCHIVES`, `TIERS`, `QUOTE`, `TALK`, and
`SOCIALS`. The markup is generated from them, so you never touch HTML.

### `ARCHIVES` — Hero 1

| Key | What it is |
| --- | --- |
| `eyebrow` | the small violet line above the headline |
| `headline` | the `<h1>`, rendered in the white-to-violet gradient |
| `dots` | the `·`-separated subhead; the separators get their own opacity |
| `copy` | the body paragraph |
| `cta` / `url` | the full-width button's label and destination |
| `icon` | key into `ICONS` for the tile above the eyebrow |
| `toggle` | the expander's label. The `↓` is added for you — don't type one |
| `note` | the line above the six rows |
| `items` | the six rows themselves |

**"They" is unexplained on purpose.** Anyone who has to ask who *they* are isn't
the buyer yet. No tooltip, no footnote, no "(the establishment)" — the line does
its filtering by being unanswered, and explaining it is the one edit that breaks
it.

### `ARCHIVES.items` — the expander rows

Each row takes `title`, `sub`, `url`, `icon`, and `accent`.

- **`url`** — set it to `"#"` and the row renders dimmed with a **Soon** badge
  and isn't clickable.
- **`accent`** — the product's own hex, the same one its cover art uses:
  Dark Psych `#f04444`, Arcane Game `#8b5cf6`, Inner Citadel `#22c9d4`,
  Primal Code `#2fd671`, Healing Protocols `#f2739b`, Peptides 101 `#3b95f0`,
  Arcane Peptides `#f0873c`, Arcane Track `#a3d93a`, Quiet Empire `#6d7cf8`.
  One hex in the data becomes five CSS custom properties on the element, so the
  icon tile, the border, the hover fill, the arrow and the focus ring all move
  together. **Don't flatten these to violet** — the colour is how someone
  recognises a product they've already seen on TikTok.
- **`icon`** — `mark`, `eye`, `pawn`, `shield`, `helix`, `protocol`,
  `molecule`, `flask`, `chart`, `whatsapp`, `instagram`, `tiktok`, `link`.
  Unknown values fall back to `link`. The product glyphs are traced from the
  matching cover art, so a row and the cover it links to are visibly the same
  product.

### `TIERS` — Heroes 2 and 3

Same shape, minus the expander: `headline`, `dots`, `copy`, `cta`, `url`,
`icon`, `accent`, and an optional `fineprint` rendered directly under the
button. Add a fourth entry and it renders as a fourth flat card — but every
card you add costs Hero 1 some of its dominance, which is the whole asset.

## Why it's laid out this way

- **Eight cards of equal weight is not a menu, it's a decision to postpone.**
  The old page asked a first-time visitor to rank eight products against each
  other before doing anything. This one asks one question — membership, yes or
  no — and hides the other six behind a tap for the minority who want to buy a
  single topic.
- **Hero 1's copy sells the library, not a feature list.** The pitch is that
  every separate product is one slice cut out of 3,300+ modules and a million
  words, and that the deepest material was never cut out at all. That argument
  gets stronger every time a new product ships; a list of six systems got
  weaker. It is also the reason the copy no longer counts anything — a number
  that has to be edited every time you launch is a number that will go stale.
- **Hero 1 is louder than Heroes 2 and 3 on purpose** — bigger padding, a
  gradient background, a violet glow, a gradient headline, and the only
  full-width filled button on the page. Heroes 2 and 3 are flat cards with
  buttons that size to their own text. Levelling that up is the one change that
  undoes the restructure.
- **The expander is collapsed on load, always.** It's a native `<details>`, so
  it needs no JavaScript to open, works with the keyboard, and can't get stuck
  half-open. Someone who wants the membership never sees six more choices.
- **"Every product below is included free in the full Archives"** sits above
  the six rows because that sentence is the argument for the membership, made
  at the exact moment someone is about to buy one product instead. It is the
  same argument as Hero 1's copy, repeated where the decision actually happens.
- **The research-use line sits under the Peptides button, not in the footer.**
  In the footer nobody reads it, and this is the one product where it has to be
  read. The footer disclaimer covers it too — that duplication is deliberate.
- **The testimonial sits under Arcane Track**, not near the peptide shop. It
  describes healing eczema. Next to a product sold "for research purposes only"
  it reads as a human-use claim for the thing being sold; next to the tracker
  it reads as what it is, which is someone describing their recovery. Moving it
  back up next to Peptides is a compliance problem, not a layout preference.
- **The identity strip is one short row**, not the old stacked block with a
  104px avatar. Every pixel it gave up is a pixel of Hero 1 that lands above
  the fold — the Archives button clears the fold on a 390×844 phone with room
  to spare.
- **WhatsApp sits last.** It's the catch for people who read everything and
  still want to talk before buying — the highest-intent visitors you have.

## The testimonial

`QUOTE` currently holds a message from your TikTok content, and it renders
directly under Hero 3 — see the layout notes above for why it is there and not
beside the peptide shop. Set `QUOTE = null` to hide the section. Two things
worth doing:

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
- Sections fade up in sequence on load, 70ms apart. It's disabled outright
  under `prefers-reduced-motion`, along with every hover transform.
- The footer disclaimer covers educational-use, research-use, and
  individual-results. Given the health claims in this niche and the existing
  TikTok account warning, keep it — and keep the shorter research-use line
  under the Peptides button as well.
- The page still loads zero images. The three hero tiles and the six expander
  rows use inline SVG glyphs, so the whole thing is one HTTP request.
