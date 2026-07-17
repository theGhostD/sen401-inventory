# Inventory Demo (SEN 401)

A small, modular Python project used for the SEN 401 lab assessment (Lab 3:
Status Accounting & Auditing, and Lab 4: Re-engineering & Migration). The
application stores an inventory of items and calculates stock statistics.

## Project Structure (v2.0, re-engineered)

```
inventory/
├── app.py              # Console UI (entry point)
├── models.py           # Item dataclass + seed data
├── controllers.py      # InventoryController — SQLite data access
├── utils.py            # Formatting helpers
├── migrate.py          # One-time list -> SQLite data migration
├── Dockerfile          # App container (python:3.12-slim)
├── docker-compose.yml  # app + sqlite-web database browser
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── docs/               # Lab reports, CSA record, reverse-engineering notes
```

## Modules

| File | Purpose |
|------|---------|
| `models.py` | `Item` frozen dataclass with validation and `line_value`; `SEED_ITEMS`. |
| `controllers.py` | `InventoryController` — owns the SQLite connection and all reads/writes. |
| `utils.py` | Presentation helpers (`format_inventory_table`, `format_currency`). |
| `app.py` | Entry point. Prints the inventory table, total stock value, highest/lowest stock, and re-order alerts. |
| `migrate.py` | Creates `inventory.db` and loads the v1.0 seed data (idempotent). |

## Usage

```bash
python3.12 migrate.py   # first run only — creates inventory.db
python3.12 app.py
```

### With Docker Compose

```bash
docker compose up --build -d
docker compose logs app          # migration + demo output
open http://localhost:8080       # sqlite-web database browser
```

## Branching Model

- `main` — stable baseline; releases are tagged here
- `dev` — maintenance work (Lab 3)
- `reengineering` — re-engineering & migration work (Lab 4)

## Releases

- **v1.0** — after completing all four maintenance tasks (Lab 3)
- **v2.0** — re-engineered: modular architecture, SQLite storage, Docker Compose (Lab 4)
