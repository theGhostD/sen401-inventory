"""Entry point for the inventory demo application.

Preventive maintenance moved all demo logic into ``main()`` behind an
``if __name__ == "__main__"`` guard so importing this module never has
side effects.
"""

from inventory import (
    format_inventory_table,
    inventory,
    low_stock_items,
    total_stock_value,
)
from utils.helpers import highest_stock_item, lowest_stock_item


def main() -> None:
    """Run the demo: list the inventory and print stock statistics."""
    print("=" * 58)
    print("                    Inventory Demo")
    print("=" * 58)
    print(format_inventory_table(inventory))

    print(f"\nTotal Stock Value : NGN {total_stock_value(inventory):,.2f}")

    top = highest_stock_item(inventory)
    bottom = lowest_stock_item(inventory)
    print(f"Highest stock     : {top['item_name']} ({top['quantity']} units)")
    print(f"Lowest stock      : {bottom['item_name']} ({bottom['quantity']} units)")

    low = low_stock_items(inventory)
    names = ", ".join(item["item_name"] for item in low) or "none"
    print(f"Re-order alert    : {names} (quantity <= 5)")


if __name__ == "__main__":
    main()
