# Lab 4 — Re-engineering & Migration

**Course:** SEN 401 — Software Configuration Management and Maintenance
**Student:** Ojekale David Akinola — Matric No: 2024/B/SENG/0241
**Repository:** <https://github.com/theGhostD/sen401-inventory>

## 1. Objective

Demonstrate advanced software maintenance: reverse engineer the Lab 3
inventory application, refactor it into modular components, migrate its
data to SQLite, and deploy it with Docker Compose. All work was done on a
`reengineering` branch and released as **v2.0**.

## 2. Reverse Engineering

The v1.0 codebase was analyzed function by function; the full write-up with
Mermaid dependency and UML-style diagrams is in
[`docs/REVERSE_ENGINEERING.md`](REVERSE_ENGINEERING.md).

**Key code smells found:**

1. **God module** — `inventory.py` mixed data storage, business logic, and presentation.
2. **Mutable global state** — every function touched the shared `inventory` list; no persistence.
3. **Loose dict records** — key typos failed only at runtime.
4. **Utility coupling** — `utils/helpers.py` imported the data module just for a type alias.
5. **No storage abstraction** — swapping storage would touch every module.

> **[SCREENSHOT 4.1]** — Rendered Mermaid module-dependency diagram (before).
> **[SCREENSHOT 4.2]** — Rendered target-architecture diagram (after).

## 3. Refactor & Modularize

The code was split by responsibility (commit `650bd58`):

| Module | Responsibility |
|--------|----------------|
| `models.py` | `Item` frozen dataclass with construction-time validation and a `line_value` property; `SEED_ITEMS` seed data. |
| `controllers.py` | `InventoryController` — repository-style class owning the SQLite connection and every read/write operation. |
| `utils.py` | Presentation-only formatting helpers; depends solely on `models`. |
| `app.py` | Thin console UI over the controller. |
| `migrate.py` | One-time data migration script. |

DRY, docstrings, and type hints applied throughout. The duplicated
`quantity * price` logic now lives in exactly one place
(`Item.line_value`).

> **[SCREENSHOT 4.3]** — IDE file explorer showing the refactored module structure.

## 4. Data Migration to SQLite

`migrate.py` creates the `items` table (with `CHECK` constraints on
quantity and price) and loads the v1.0 seed data. It is idempotent — if
rows already exist it does nothing.

```
$ python3.12 migrate.py
migrated: Laptop (id=1)
migrated: Mouse (id=2)
migrated: Keyboard (id=3)
migrated: Monitor (id=4)
migrated: USB Cable (id=5)

Migration complete: 5 items -> inventory.db
```

Read and write paths were verified against the database:

```
$ sqlite3 inventory.db "SELECT * FROM items;"
1|Laptop|4|350000.0
2|Mouse|25|4500.0
3|Keyboard|18|12000.0
4|Monitor|7|95000.0
5|USB Cable|60|1500.0
```

The application output is identical to v1.0 (total stock value
NGN 2,483,500.00) — proof the migration preserved behaviour.

> **[SCREENSHOT 4.4]** — Terminal showing `migrate.py` output and the SQLite query results.
> **[SCREENSHOT 4.5]** — Terminal showing `python3.12 app.py` reading from SQLite.

## 5. Docker Compose Deployment

Two services are orchestrated by `docker-compose.yml`:

| Service | Image | Role |
|---------|-------|------|
| `app` | built from local `Dockerfile` (python:3.12-slim) | Runs `migrate.py` then `app.py`; stays alive so the service is inspectable. |
| `db-browser` | `coleifer/sqlite-web` | Web UI for the database on <http://localhost:8080>. |

Both mount the shared `inventory-data` volume, so the browser sees exactly
the database the app writes — the two containers communicate through the
persisted configuration item.

```bash
docker compose up --build -d
docker compose ps            # both services running
docker compose logs app     # migration + demo output
```

> **[SCREENSHOT 4.6]** — `docker compose up` build/run output.
> **[SCREENSHOT 4.7]** — `docker compose ps` showing both containers running.
> **[SCREENSHOT 4.8]** — sqlite-web at localhost:8080 displaying the items table.

## 6. Version Control

```
650bd58 Lab 4 steps 2-3: refactor into models/controllers/utils and migrate to SQLite
7df6f65 Lab 4 step 1: reverse engineering analysis with dependency diagrams
```

Work merged from `reengineering` into `main` and tagged **v2.0**.

## 7. Observations

- Reverse engineering first (before touching code) meant the refactor was a
  checklist, not an exploration — each code smell mapped to one remedy.
- The repository-style controller made the SQLite migration invisible to
  the UI layer: `app.py` changed only its import lines.
- Docker Compose turned "works on my machine" into a reproducible
  deployment: one command builds Python 3.12, installs dependencies,
  migrates data, and serves a database browser.
