"""Data module for the inventory demo application.

Owns the in-memory inventory data set and every operation that reads or
mutates it. Refactored during preventive maintenance: shared ``Item`` type
alias, one public function per responsibility, and docstrings throughout.

Requires Python 3.12+ (PEP 695 ``type`` statement).
"""

# A single inventory entry as stored in the data set.
type Item = dict[str, str | int | float]

#: The demo data set. Mutated only through :func:`add_item`.
inventory: list[Item] = [
    {"item_name": "Laptop", "quantity": 4, "price": 350000.00},
    {"item_name": "Mouse", "quantity": 25, "price": 4500.00},
    {"item_name": "Keyboard", "quantity": 18, "price": 12000.00},
    {"item_name": "Monitor", "quantity": 7, "price": 95000.00},
    {"item_name": "USB Cable", "quantity": 60, "price": 1500.00},
]


def line_value(item: Item) -> float:
    """Return the stock value of a single item (quantity x unit price)."""
    return item["quantity"] * item["price"]


def total_stock_value(items: list[Item]) -> float:
    """Return the total stock value across ``items``.

    The corrective fix in Lab 3 ensures quantity is included: the starter
    version summed unit prices only.
    """
    return sum(line_value(item) for item in items)


def low_stock_items(items: list[Item], threshold: int = 5) -> list[Item]:
    """Return items whose quantity is at or below ``threshold``."""
    return [item for item in items if item["quantity"] <= threshold]


def format_inventory_table(items: list[Item]) -> str:
    """Render ``items`` as an aligned console table with currency formatting."""
    if not items:
        return "(inventory is empty)"
    header = f"{'Item':<12} {'Qty':>5} {'Unit Price (NGN)':>18} {'Line Value (NGN)':>18}"
    lines = [header, "-" * len(header)]
    for item in items:
        lines.append(
            f"{item['item_name']:<12} {item['quantity']:>5} "
            f"{item['price']:>18,.2f} {line_value(item):>18,.2f}"
        )
    return "\n".join(lines)


def add_item(item_name: str, quantity: int, price: float) -> None:
    """Validate and append a new item to the inventory.

    Raises:
        ValueError: if any field is missing, negative, or the wrong type.
    """
    if not item_name or not isinstance(item_name, str):
        raise ValueError("item_name must be a non-empty string")
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("quantity must be a non-negative integer")
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("price must be a non-negative number")
    inventory.append({"item_name": item_name, "quantity": quantity, "price": price})
