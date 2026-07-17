"""Business logic and data access for the inventory application.

``InventoryController`` is a repository-style controller: it owns the
SQLite connection and exposes every read/write operation the UI needs.
Re-engineered in Lab 4 to replace the mutable module-level list from v1.0.
"""

import os
import sqlite3
from pathlib import Path

from models import Item

#: Database location; overridable so Docker can mount a volume.
DB_PATH = Path(os.environ.get("INVENTORY_DB", "inventory.db"))

_SCHEMA = """
CREATE TABLE IF NOT EXISTS items (
    item_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT    NOT NULL,
    quantity  INTEGER NOT NULL CHECK (quantity >= 0),
    price     REAL    NOT NULL CHECK (price >= 0)
);
"""


class InventoryController:
    """All inventory operations, backed by SQLite."""

    def __init__(self, db_path: Path | str = DB_PATH) -> None:
        """Open (and if necessary create) the database at ``db_path``."""
        self._conn = sqlite3.connect(db_path)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute(_SCHEMA)
        self._conn.commit()

    # -- reads ------------------------------------------------------------

    def all_items(self) -> list[Item]:
        """Return every item, ordered by primary key."""
        rows = self._conn.execute(
            "SELECT item_id, item_name, quantity, price FROM items ORDER BY item_id"
        ).fetchall()
        return [self._to_item(row) for row in rows]

    def total_stock_value(self) -> float:
        """Return the total stock value (sum of quantity x price)."""
        row = self._conn.execute(
            "SELECT COALESCE(SUM(quantity * price), 0) AS total FROM items"
        ).fetchone()
        return float(row["total"])

    def low_stock_items(self, threshold: int = 5) -> list[Item]:
        """Return items whose quantity is at or below ``threshold``."""
        rows = self._conn.execute(
            "SELECT item_id, item_name, quantity, price FROM items"
            " WHERE quantity <= ? ORDER BY quantity",
            (threshold,),
        ).fetchall()
        return [self._to_item(row) for row in rows]

    def highest_stock_item(self) -> Item | None:
        """Return the item with the largest quantity, or ``None`` if empty."""
        row = self._conn.execute(
            "SELECT item_id, item_name, quantity, price FROM items"
            " ORDER BY quantity DESC LIMIT 1"
        ).fetchone()
        return self._to_item(row) if row else None

    def lowest_stock_item(self) -> Item | None:
        """Return the item with the smallest quantity, or ``None`` if empty."""
        row = self._conn.execute(
            "SELECT item_id, item_name, quantity, price FROM items"
            " ORDER BY quantity ASC LIMIT 1"
        ).fetchone()
        return self._to_item(row) if row else None

    # -- writes -----------------------------------------------------------

    def add_item(self, item: Item) -> Item:
        """Persist a validated ``Item`` and return it with its new id."""
        cursor = self._conn.execute(
            "INSERT INTO items (item_name, quantity, price) VALUES (?, ?, ?)",
            (item.item_name, item.quantity, item.price),
        )
        self._conn.commit()
        return Item(item.item_name, item.quantity, item.price, cursor.lastrowid)

    def close(self) -> None:
        """Close the underlying database connection."""
        self._conn.close()

    # -- internal ---------------------------------------------------------

    @staticmethod
    def _to_item(row: sqlite3.Row) -> Item:
        """Convert a database row into an ``Item``."""
        return Item(
            item_name=row["item_name"],
            quantity=row["quantity"],
            price=row["price"],
            item_id=row["item_id"],
        )
