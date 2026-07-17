"""Entry point for the inventory application (v2.0, re-engineered).

The console UI talks only to :class:`controllers.InventoryController`;
data lives in SQLite and formatting lives in :mod:`utils`.
"""

from controllers import InventoryController
from utils import format_currency, format_inventory_table


def main() -> None:
    """Run the demo: list the inventory and print stock statistics."""
    controller = InventoryController()
    items = controller.all_items()

    print("=" * 62)
    print("                Inventory Demo (v2.0, SQLite)")
    print("=" * 62)
    print(format_inventory_table(items))

    print(f"\nTotal Stock Value : {format_currency(controller.total_stock_value())}")

    top = controller.highest_stock_item()
    bottom = controller.lowest_stock_item()
    if top and bottom:
        print(f"Highest stock     : {top.item_name} ({top.quantity} units)")
        print(f"Lowest stock      : {bottom.item_name} ({bottom.quantity} units)")

    low = controller.low_stock_items()
    names = ", ".join(item.item_name for item in low) or "none"
    print(f"Re-order alert    : {names} (quantity <= 5)")

    controller.close()


if __name__ == "__main__":
    main()
