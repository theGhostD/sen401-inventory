# Lab 3 — Status Accounting & Auditing

**Course:** SEN 401 — Software Configuration Management and Maintenance
**Student:** `[YOUR FULL NAME]` — Matric No: `[YOUR MATRIC NUMBER]`
**Repository:** <https://github.com/theGhostD/sen401-inventory>

## 1. Objective

Track and document every change in a software project using Git, applying
Software Configuration Status Accounting (CSA): who changed what, when, on
which branch, and in which release it shipped.

## 2. Repository & Project Setup

A new repository (`sen401-inventory`) was initialized with the following files:

| File | Purpose |
|------|---------|
| `inventory.py` | List of items (`item_name`, `quantity`, `price`) plus stock-value functions. |
| `app.py` | Reads the inventory and reports total stock value and statistics. |
| `utils/helpers.py` | `highest_stock_item()` / `lowest_stock_item()` helpers. |
| `requirements.txt` | Python dependencies (standard library only). |
| `README.md` | Project description and usage instructions. |

```bash
git init -b main
git add -A && git commit -m "Initial commit: starter inventory project"
git checkout -b dev
```

> **[SCREENSHOT 3.1]** — IDE file explorer showing the project structure.

## 3. Maintenance Tasks Performed (on `dev`)

| Type | Change | Commit |
|------|--------|--------|
| Corrective | `total_stock_value()` summed unit prices only, under-reporting stock value (463,000 → **2,483,500** for the seed data). Fixed to quantity × price; `add_item()` now validates input. | `e90144e` |
| Adaptive | Python 3.12 type hints (PEP 695 `type Item` alias); new `low_stock_items()` re-order alert feature. | `e9efde0` |
| Perfective | `format_inventory_table()` — aligned columns, thousands separators, per-line value; labelled output sections. | `df06490` |
| Preventive | Refactor: DRY `line_value()` helper, docstrings throughout, `main()` guard, clear `ValueError` on empty inventory. | `7cb86ec` |

> **[SCREENSHOT 3.2]** — Terminal output of `python3.12 app.py` after all maintenance.

## 4. Version Control

All maintenance was committed to `dev` with descriptive messages, merged
into `main` with `--no-ff` (preserving the branch structure), and tagged:

```bash
git checkout main
git merge --no-ff dev
git tag -a v1.0 -m "v1.0: inventory app after all four maintenance types"
```

## 5. Git Change Logs

Generated with:

```bash
git log --pretty=format:"%h | %an | %ad | %s" --date=short > changelog.txt
```

Contents of `changelog.txt`:

```
3d2a33a | David Ojekale | 2026-07-17 | Merge branch 'dev': all four maintenance tasks complete
7cb86ec | David Ojekale | 2026-07-17 | Preventive maintenance: refactor for modularity and maintainability
df06490 | David Ojekale | 2026-07-17 | Perfective maintenance: currency-formatted inventory table
e9efde0 | David Ojekale | 2026-07-17 | Adaptive maintenance: Python 3.12 type hints and low-stock alert feature
e90144e | David Ojekale | 2026-07-17 | Corrective maintenance: fix total stock value calculation and input bugs
367ca71 | David Ojekale | 2026-07-17 | Initial commit: starter inventory project
```

`git log --oneline --graph --all`:

```
*   3d2a33a Merge branch 'dev': all four maintenance tasks complete
|\
| * 7cb86ec Preventive maintenance: refactor for modularity and maintainability
| * df06490 Perfective maintenance: currency-formatted inventory table
| * e9efde0 Adaptive maintenance: Python 3.12 type hints and low-stock alert feature
| * e90144e Corrective maintenance: fix total stock value calculation and input bugs
|/
* 367ca71 Initial commit: starter inventory project
```

> **[SCREENSHOT 3.3]** — Terminal showing `git log --oneline`.
> **[SCREENSHOT 3.4]** — Terminal showing `git log --graph --all`.

## 6. Configuration Status Accounting

The full CSA record — configuration items, commit-to-task traceability
table, branch status, and release status — is documented in
[`docs/CSA.md`](CSA.md). Key observation: because each maintenance category
was one commit, the Git history itself *is* the status-accounting ledger;
`changelog.txt` and `CSA.md` are exported views of it.

> **[SCREENSHOT 3.5]** — GitHub repository showing commits, branches, and the v1.0 release.

## 7. Observations

- Descriptive one-commit-per-task messages made traceability trivial — no
  extra tooling was needed to map commits to maintenance categories.
- `--no-ff` merging preserved the shape of the workflow in the graph, which
  is exactly what an auditor needs to see.
- Exporting `changelog.txt` into the repository makes the audit record a
  configuration item itself, versioned like the code it describes.
