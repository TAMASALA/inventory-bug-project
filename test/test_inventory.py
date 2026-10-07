from inventory import (
    calculate_total_price,
    apply_discount,
    get_available_items,
    find_item,
)


def test_calculate_total_price():
    items = [
        {
            "name": "Laptop",
            "price": 1000,
            "quantity": 2,
        },
        {
            "name": "Mouse",
            "price": 50,
            "quantity": 3,
        },
    ]

    assert calculate_total_price(items) == 2150


def test_apply_discount():
    assert apply_discount(1000, 10) == 900
    assert apply_discount(500, 20) == 400


def test_get_available_items():
    items = [
        {
            "name": "Laptop",
            "price": 1000,
            "quantity": 2,
        },
        {
            "name": "Mouse",
            "price": 50,
            "quantity": 0,
        },
        {
            "name": "Keyboard",
            "price": 80,
            "quantity": 5,
        },
    ]

    result = get_available_items(items)

    assert len(result) == 2
    assert result[0]["name"] == "Laptop"
    assert result[1]["name"] == "Keyboard"


def test_find_item():
    items = [
        {
            "name": "Laptop",
            "price": 1000,
            "quantity": 2,
        },
        {
            "name": "Mouse",
            "price": 50,
            "quantity": 3,
        },
    ]

    result = find_item(items, "Mouse")

    assert result is not None
    assert result["price"] == 50
    assert result["quantity"] == 3


def test_find_missing_item():
    items = [
        {
            "name": "Laptop",
            "price": 1000,
            "quantity": 2,
        }
    ]

    assert find_item(items, "Phone") is None