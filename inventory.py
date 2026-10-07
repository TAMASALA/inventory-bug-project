def calculate_total_price(items):
    """
    Calculate the total price of inventory items.

    Each item must contain:
    {
        "name": str,
        "price": float,
        "quantity": int
    }
    """

    total = 0

    for item in items:
        total += item["price"] * item["quantity"]

    return total


def apply_discount(total, discount_percent):
    """Apply a percentage discount to the total."""

    discount = total * discount_percent / 100

    return total - discount


def get_available_items(items):
    """Return items that have stock available."""

    return [
        item
        for item in items
        if item["quantity"] > 0
    ]


def find_item(items, name):
    """Find an item by name, case-insensitively."""

    for item in items:
        if item["name"].lower() == name.lower():
            return item

    return None