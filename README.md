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

Designed for **1440px desktop**. One committed light theme, deliberately: this
is a tool accountants keep open all day, not a site to theme.

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

A neutral finance workspace with quiet Excel familiarity: white surfaces, thin
`#E4E7EC` borders, compact tables, right-aligned tabular numerals. Roughly 80%
neutral, 15% functional status colour, 5% brand.

Green marks matched, approved, normalized, the selected tab and every primary
action. Red is blocking and destructive. Amber is a difference worth reviewing
that does not necessarily block. Grey is pending and skipped. Blue is
informational and in-progress. CureFoods gold appears only on the logo, the
active navigation item and small brand markers — never on a warning, so amber
stays unmistakable.

Contrast is measured rather than assumed: body ink 14.7:1, secondary ink 5.0:1,
and every colour that carries readable text clears 4.5:1. The two brand-weight
tones (`#B68A2F`, `#C97812`) are graphical only — icons, borders and rules —
and a separate readable tone carries the words.

## Note on the Oracle push fields

The source field reference marks section 10 (Oracle Push Fields) as *not
present in the supplied payload*. Those fields are represented in the prototype
from the documented contract, and the caveat is recorded in the design system.
