# inventory.py - data module for the inventory demo app
# Adaptive maintenance: Python 3.12 type hints + low-stock alert feature

type Item = dict[str, str | int | float]

inventory: list[Item] = [
    {"item_name": "Laptop", "quantity": 4, "price": 350000.00},
    {"item_name": "Mouse", "quantity": 25, "price": 4500.00},
    {"item_name": "Keyboard", "quantity": 18, "price": 12000.00},
    {"item_name": "Monitor", "quantity": 7, "price": 95000.00},
    {"item_name": "USB Cable", "quantity": 60, "price": 1500.00},
]


def low_stock_items(items: list[Item], threshold: int = 5) -> list[Item]:
    # Adaptive maintenance: new re-order alert feature
    return [item for item in items if item["quantity"] <= threshold]


def total_stock_value(items: list[Item]) -> float:
    total = 0
    for item in items:
        # Corrective maintenance: value = quantity * price (price alone
        # under-reported the total stock value)
        total += item["quantity"] * item["price"]
    return total


def format_inventory_table(items: list[Item]) -> str:
    # Perfective maintenance: aligned table with currency formatting
    if not items:
        return "(inventory is empty)"
    header = f"{'Item':<12} {'Qty':>5} {'Unit Price (NGN)':>18} {'Line Value (NGN)':>18}"
    lines = [header, "-" * len(header)]
    for item in items:
        value = item["quantity"] * item["price"]
        lines.append(
            f"{item['item_name']:<12} {item['quantity']:>5} "
            f"{item['price']:>18,.2f} {value:>18,.2f}"
        )
    return "\n".join(lines)


def add_item(item_name: str, quantity: int, price: float) -> None:
    # Corrective maintenance: validate input before storing
    if not item_name or not isinstance(item_name, str):
        raise ValueError("item_name must be a non-empty string")
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("quantity must be a non-negative integer")
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("price must be a non-negative number")
    inventory.append({"item_name": item_name, "quantity": quantity, "price": price})
