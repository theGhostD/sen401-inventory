"""Domain models for the inventory application.

Re-engineered in Lab 4: items are typed ``dataclass`` records instead of
loose dictionaries, so field typos fail immediately and every module shares
one definition of what an item is.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    """A single inventory item.

    Attributes:
        item_name: Human-readable product name (non-empty).
        quantity: Units currently in stock (>= 0).
        price: Unit price in NGN (>= 0).
        item_id: Database primary key; ``None`` until persisted.
    """

    item_name: str
    quantity: int
    price: float
    item_id: int | None = None

    def __post_init__(self) -> None:
        """Validate fields at construction time."""
        if not self.item_name or not isinstance(self.item_name, str):
            raise ValueError("item_name must be a non-empty string")
        if not isinstance(self.quantity, int) or self.quantity < 0:
            raise ValueError("quantity must be a non-negative integer")
        if not isinstance(self.price, (int, float)) or self.price < 0:
            raise ValueError("price must be a non-negative number")

    @property
    def line_value(self) -> float:
        """Stock value of this item (quantity x unit price)."""
        return self.quantity * self.price


#: Seed data used by the migration script (mirrors the v1.0 Python list).
SEED_ITEMS: list[Item] = [
    Item("Laptop", 4, 350000.00),
    Item("Mouse", 25, 4500.00),
    Item("Keyboard", 18, 12000.00),
    Item("Monitor", 7, 95000.00),
    Item("USB Cable", 60, 1500.00),
]
