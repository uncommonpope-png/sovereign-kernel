# Learn From Real Files (Aria's teaching skill)

Betty teaches by showing the REAL file, never a summary. When you are given a file to learn from, read the file itself. Do not answer from a briefing.

## The real catalog
- The Soul Economy catalog lives in this repo as `soul-economy-catalog.json` — 282 real entries, straight from the repo. Read it before you write any code that touches it.
- A real entry looks like this (Architect soul):
  `{"type": "soul", "name": "Architect", "desc": "…", "plt": "0.8/0.5/0.3", "tags": […], "file": "…", "image": "…"}`
- PLT is a STRING: "profit/love/tax", e.g. "0.8/0.5/0.3". There is NO `pltScore` field anywhere. To score an entry, split `plt` on "/" and take the FIRST number as the Profit score.
- Every entry has `type`, `name`, `desc`, `plt`, `tags`. Use those exact field names. Never invent a field.

## What your last code got wrong (learn this, do not repeat it)
Your first search.js draft failed `node --check` with: `SyntaxError: Unexpected token 'return'` — because `const filterByType = t =>` was followed by a bare `return`. An arrow function body is an expression or a `{ }` block, never a bare return.
It also filtered a variable called `results` that did not exist, and read `item.pltScore`, which does not exist. One shared `data` array, real field names, close the module, export the functions.

## The rule
A file is NOT done until it passes `node --check` AND runs against real entries from `soul-economy-catalog.json`. If it does not run, say so and fix it — do not present broken code as finished.
