# CureFoods Payables — Three-Way Match Console

A redesign of the desktop accounts-payable console that three-way-matches
**Purchase Orders → Goods Received Notes → vendor invoices**, then prepares the
eligible invoices for Oracle.

The matching logic, routes, permissions and backend behaviour are unchanged.
This repository is the **interface** work: a clickable high-fidelity prototype
plus the design system behind it.

## What's here

| File | What it is |
| --- | --- |
| [`payables-match-console.html`](payables-match-console.html) | The clickable prototype. Seven screens, 30 sample cases, real interaction — tabs, filters, dialogs, toasts, keyboard focus. |
| [`payables-design-system.html`](payables-design-system.html) | Design tokens, component states, per-screen information hierarchy, the PO/GRN technical-field lists, and the phase-one UAT scope. |
| `index.html` | Symlink to the prototype, so the local server opens it at `/`. |
| `.claude/serve.js` | A 20-line static file server for local viewing. |

Each HTML file is fully self-contained — one file, no build step, no bundler,
no runtime dependencies. Inter and IBM Plex Mono load from Google Fonts;
everything else is inline.

## Running it

```
node .claude/serve.js
```

Then open <http://localhost:8781>. Or just open either `.html` file directly in
a browser — they work from the filesystem too.

Designed for **1440px desktop** and verified at 1440×900, 1280×800 and down to
a 1024px laptop. One committed light theme, deliberately: this is a tool
accountants keep open all day, not a site to theme.

## The users

Non-technical accountants who live in Excel, working across several entities of
the same parent — CureFoods, Cake Zone, Olio Pizza, Millet Express, Nomad
Pizza. So it reads as one neutral finance product, not a CureFoods marketing
site, and not a literal copy of a spreadsheet.

## Scope

`PO → GRN → Invoice → Normalization → Rule engine → Resolution → Oracle push`

## Interface principles

- **Every data layer is labelled.** "Recorded in the PO", "Extracted from
  invoice", "Normalized for comparison" — an OCR reading is never presented as
  fact, and a normalized value always shows its conversion in words
  (`420 nos × 2 kg = 840 kg`).
- **No raw JSON, ever.** Business-facing fields come first; internal IDs,
  timestamps, match IDs and attempt metadata sit inside a collapsed
  **Technical details** panel.
- **Status is never colour alone.** Every state carries a word and a glyph as
  well as a tint.
- **Nothing leaves the building without a preview.** Anything that sends data,
  triggers processing or cannot be undone is one confirmation away, and the
  dialog states exactly what will happen and to whom.
- **One date format** (`17 Jul 2026, 1:02 PM`), rupees with Indian digit
  grouping, and `Yes` / `No` / `Available` / `Not available` in place of
  `true` / `false`.

## Visual direction

A white finance workspace with quiet Excel familiarity. Page, rail, content and
cards are all `#FFFFFF`; the only tinted surfaces are a `#F8FAF9` table header
and a `#F7F8F8` band where two areas genuinely need separating — a card footer,
a row hover, the neutral canvas behind a scanned invoice page. Borders are a
thin `#E4E7EC`. No cream, no beige, no warm grey. Roughly 80% white surfaces
and ink, 15% functional status colour, 5% green.

**Green is the product colour.** The 28px mark in the rail is a solid `#2F6B4F`
tile with a white glyph, the active sidebar item is a soft green fill with a
green left rule, and matched or safely normalized values read green.
**Selection is outlined, never filled**: a pressed filter pill keeps its white
background and states itself with a 2px green outline and a green label, so the
status dot inside it — red for blocking, amber for flags, blue for notes, grey
for skipped, green for passed — stays readable; the selected tab carries a green
label and a 2.5px green underline on white.

**Red is blocking** — a commercial mismatch, a missing required Oracle field, a
destructive action. **Amber appears only when something genuinely needs
attention**: a GST mismatch, a low OCR confidence, a non-blocking variance,
"Needs attention" — and it appears as a glyph, a word, a badge or a 3px left
rule, never as a large fill. A warning banner is a white card with a 3px amber
left rule, an amber icon and an amber heading. Grey is pending and skipped;
blue is informational and in progress.

Contrast is measured rather than assumed:

| Pair | Ratio |
| --- | --- |
| `--ink` `#1F2933` on white | 14.8:1 |
| `--ink-2` `#667085` on white | 5.0:1 |
| `--green-deep` `#255840` on white | 8.2:1 |
| `--green-deep` on `--green-bg` `#EAF4EE` | 7.3:1 |
| white on `--green` `#2F6B4F` | 6.3:1 |
| `--red` `#B42318` on white | 6.6:1 |
| `--red-deep` on `--red-bg` `#FEECEB` | 7.6:1 |
| `--amber` `#A15C16` on white | 5.9:1 |
| `--green` `#2F6B4F` on white | 6.3:1 |

Every tone that carries readable text clears 4.5:1. `--ink-3` `#98A2B3` is the
disabled grey and never carries a readable value.

Interface text sits at 13–14px, table headers at 12px, and no interactive
control is shorter than 34px. At a 1280px laptop width the dashboard toolbar
wraps to a second row rather than shrinking a control: Brand, Supplier and Dates
keep their visible labels at every width, Export and Columns stay reachable, and
the table scrolls horizontally with PO number, GRN number and status pinned.

## Scrolling

The shell is a full-height flex layout. `.frame` is `100vh` with
`overflow:hidden`; the rail and the main column both run the full height with
`min-height:0`; and exactly **one** element scrolls vertically — the content
area beneath the case header. Because the case header and the tab bar are
siblings of that scroller rather than children, they stay pinned without a
single `position:sticky` rule, and the sidebar user profile stays pinned to the
bottom of the rail.

Wide comparison tables scroll horizontally inside their own card and never
widen the page; every pane sets `min-width:0`, so a long identifier cannot force
a page-level horizontal scrollbar. Dashboard pagination sits at the bottom of
the table and is always reachable; a right-side action panel un-sticks itself
when it is taller than the scrollport, so its bottom is never clipped.

The one deliberate second scroller is the extracted-details pane on the invoice
screen, which scrolls against the document viewer beside it with both pane
toolbars pinned. Below 1080px even that collapses: the PDF and the details stack
and the page scrolls normally.

## Note on the Oracle push fields

The source field reference marks section 10 (Oracle Push Fields) as *not
present in the supplied payload*. Those fields are represented in the prototype
from the documented contract, and the caveat is recorded in the design system.
