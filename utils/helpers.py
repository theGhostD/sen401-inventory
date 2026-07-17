"""Utility helpers for the inventory demo application.

Kept separate from the data module so generic lookups can be reused by any
caller without importing the mutable data set itself.
"""

from inventory import Item


def highest_stock_item(items: list[Item]) -> Item:
    """Return the item with the largest quantity.

    Raises:
        ValueError: if ``items`` is empty.
    """
    if not items:
        raise ValueError("Cannot find highest stock item of an empty inventory")
    return max(items, key=lambda item: item["quantity"])


def lowest_stock_item(items: list[Item]) -> Item:
    """Return the item with the smallest quantity.

    Raises:
        ValueError: if ``items`` is empty.
    """
    if not items:
        raise ValueError("Cannot find lowest stock item of an empty inventory")
    return min(items, key=lambda item: item["quantity"])
