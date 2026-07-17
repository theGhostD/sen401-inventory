# Inventory Demo (SEN 401)

A small, modular Python project used for the SEN 401 lab assessment (Lab 3:
Status Accounting & Auditing, and Lab 4: Re-engineering & Migration). The
application stores an inventory of items and calculates stock statistics.

## Project Structure

```
inventory/
├── app.py              # Main script — reads inventory and reports stock value
├── inventory.py        # Data module — item records + stock value functions
├── utils/
│   ├── __init__.py
│   └── helpers.py      # highest_stock_item() / lowest_stock_item() helpers
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── docs/               # Lab reports and CSA documentation
```

## Modules

| File | Purpose |
|------|---------|
| `app.py` | Entry point. Prints all items, the total stock value, and the highest/lowest stocked items. |
| `inventory.py` | Holds the `inventory` list (each item has `item_name`, `quantity`, `price`) plus `total_stock_value()` and `add_item()`. |
| `utils/helpers.py` | `highest_stock_item()` and `lowest_stock_item()` helpers. |

## Usage

```bash
python3 app.py
```

## Branching Model

- `main` — stable baseline; releases are tagged here
- `dev` — maintenance and development work

## Releases

- **v1.0** — after completing all four maintenance tasks (Lab 3)
