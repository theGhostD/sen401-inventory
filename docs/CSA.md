# Configuration Status Accounting (CSA) — Inventory Project

Configuration Status Accounting records the state of every configuration
item over the project's life: what changed, when, by whom, on which branch,
and in which release it shipped.

## Configuration Items

| CI | Type | Location |
|----|------|----------|
| `app.py` | Source | repository root |
| `inventory.py` | Source | repository root |
| `utils/helpers.py` | Source | `utils/` |
| `requirements.txt` | Configuration | repository root |
| `README.md` | Documentation | repository root |
| `changelog.txt` | Record | repository root |

## Commit-to-Task Traceability

| Commit | Branch | Maintenance task | Configuration items affected | Release |
|--------|--------|------------------|------------------------------|---------|
| `367ca71` | `main` | Baseline (starter code) | all | — |
| `e90144e` | `dev` | **Corrective** — fixed total stock value calculation (quantity × price) and input validation | `inventory.py` | v1.0 |
| `e9efde0` | `dev` | **Adaptive** — Python 3.12 type hints, new low-stock alert feature | `inventory.py`, `app.py` | v1.0 |
| `df06490` | `dev` | **Perfective** — currency-formatted inventory table | `inventory.py`, `app.py` | v1.0 |
| `7cb86ec` | `dev` | **Preventive** — refactor, DRY `line_value()`, docstrings, `main()` guard | `inventory.py`, `app.py`, `utils/helpers.py` | v1.0 |
| `3d2a33a` | `main` | Merge `dev` → `main` (all maintenance complete) | — | v1.0 |

## Branch Status

| Branch | Purpose | Status |
|--------|---------|--------|
| `main` | Stable baseline; releases tagged here | at `3d2a33a`, tagged `v1.0` |
| `dev` | Maintenance work | merged into `main` |

## Release Status

| Release | Commit | Contents |
|---------|--------|----------|
| `v1.0` | `3d2a33a` | Starter code + all four maintenance tasks |

## Audit Trail

The full audit trail is reproducible from the repository itself:

```bash
git log --oneline            # every change, newest first
git log --graph --all        # branch/merge structure
git tag -n                   # release baselines
cat changelog.txt            # exported log (commit, author, date, subject)
```
