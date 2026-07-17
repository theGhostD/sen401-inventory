"""One-time data migration: v1.0 Python-list inventory -> SQLite.

Lab 4 migration step. Creates ``inventory.db`` (or the path in the
``INVENTORY_DB`` environment variable) and loads the v1.0 seed data into
the ``items`` table. Safe to re-run: it skips migration if the table
already contains rows.
"""

from controllers import DB_PATH, InventoryController
from models import SEED_ITEMS


def migrate() -> None:
    """Create the schema and load seed data if the database is empty."""
    controller = InventoryController(DB_PATH)
    existing = controller.all_items()
    if existing:
        print(f"{DB_PATH}: already migrated ({len(existing)} items) — nothing to do")
        controller.close()
        return

    for item in SEED_ITEMS:
        saved = controller.add_item(item)
        print(f"migrated: {saved.item_name} (id={saved.item_id})")

    print(f"\nMigration complete: {len(SEED_ITEMS)} items -> {DB_PATH}")
    controller.close()


if __name__ == "__main__":
    migrate()
