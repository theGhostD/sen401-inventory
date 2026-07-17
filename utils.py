"""Presentation helpers for the inventory application.

Depends only on :mod:`models` — no data access, no global state — so it can
be reused by any front end (console, API, tests).
"""

from models import Item


def format_inventory_table(items: list[Item]) -> str:
    """Render ``items`` as an aligned console table with currency formatting."""
    if not items:
        return "(inventory is empty)"
    header = f"{'ID':<4} {'Item':<12} {'Qty':>5} {'Unit Price (NGN)':>18} {'Line Value (NGN)':>18}"
    lines = [header, "-" * len(header)]
    for item in items:
        lines.append(
            f"{item.item_id or '-':<4} {item.item_name:<12} {item.quantity:>5} "
            f"{item.price:>18,.2f} {item.line_value:>18,.2f}"
        )
    return "\n".join(lines)


def format_currency(amount: float) -> str:
    """Format ``amount`` as an NGN currency string."""
    return f"NGN {amount:,.2f}"
