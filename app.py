# app.py - main script that reads from inventory.py and reports stock value

from inventory import inventory, low_stock_items, total_stock_value
from utils.helpers import highest_stock_item, lowest_stock_item

print("=== Inventory Demo ===")
print("Items:", inventory)
print("Total Stock Value:", total_stock_value(inventory))

top = highest_stock_item(inventory)
bottom = lowest_stock_item(inventory)
print("Highest stock:", top["item_name"], "(", top["quantity"], ")")
print("Lowest stock:", bottom["item_name"], "(", bottom["quantity"], ")")

low = low_stock_items(inventory)
print("Re-order alert (quantity <= 5):", [item["item_name"] for item in low])
