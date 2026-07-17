# inventory.py - data module for the inventory demo app

inventory = [
    {"item_name": "Laptop", "quantity": 4, "price": 350000.00},
    {"item_name": "Mouse", "quantity": 25, "price": 4500.00},
    {"item_name": "Keyboard", "quantity": 18, "price": 12000.00},
    {"item_name": "Monitor", "quantity": 7, "price": 95000.00},
    {"item_name": "USB Cable", "quantity": 60, "price": 1500.00},
]


def total_stock_value(items):
    total = 0
    for item in items:
        # Corrective maintenance: value = quantity * price (price alone
        # under-reported the total stock value)
        total += item["quantity"] * item["price"]
    return total


def add_item(item_name, quantity, price):
    # Corrective maintenance: validate input before storing
    if not item_name or not isinstance(item_name, str):
        raise ValueError("item_name must be a non-empty string")
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("quantity must be a non-negative integer")
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("price must be a non-negative number")
    inventory.append({"item_name": item_name, "quantity": quantity, "price": price})
