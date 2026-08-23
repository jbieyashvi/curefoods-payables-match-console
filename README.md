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

Designed for **1440px desktop** and verified down to a 1280px laptop. One
committed light theme, deliberately: this is a tool accountants keep open all
day, not a site to theme.

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

A neutral finance workspace with quiet Excel familiarity: an off-white `#F7F8F6`
ground, white card and table surfaces, thin `#E4E7EC` borders, compact tables,
right-aligned tabular numerals. Roughly 80% neutral surfaces and ink, 15%
functional status colour, 5% product mark.

**Green is selection and success.** The active sidebar item is a soft green fill
with a green left rule, a pressed filter pill is a solid green fill with white
text, the selected tab carries a green label and a green underline, and matched
or safely normalized values read green. **Red is blocking** — a commercial
mismatch, a missing required Oracle field, a destructive action. **Amber appears
only when something genuinely needs attention**: a GST mismatch, a low OCR
confidence, a non-blocking variance, "Needs attention". It never marks a
selection, a navigation item or a build marker. Grey is pending and skipped;
blue is informational and in progress.

CureFoods gold survives in exactly one place — the 28px product mark in the
rail — so nothing competes with green for selection or with amber for
attention.

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
| `--amber` `#A15C16` on `--amber-bg` `#FFF7ED` | 4.9:1 |

Every tone that carries readable text clears 4.5:1. `--gold-brand` `#B68A2F` is
graphical only and carries no words.

Interface text sits at 13–14px, table headers at 12px, and no interactive
control is shorter than 34px. At a 1280px laptop width the dashboard toolbar
wraps to a second row rather than shrinking a control: Brand, Supplier and Dates
keep their visible labels at every width, Export and Columns stay reachable, and
the table scrolls horizontally with PO number, GRN number and status pinned.

## Note on the Oracle push fields

The source field reference marks section 10 (Oracle Push Fields) as *not
present in the supplied payload*. Those fields are represented in the prototype
from the documented contract, and the caveat is recorded in the design system.
