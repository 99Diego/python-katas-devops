from app.domain.shopping import get_total


def test_get_total_with_tax():
    costs = {"socks": 5, "shoes": 60}
    items = ["socks", "shoes"]
    tax = 0.09

    assert get_total(costs, items, tax) == 70.85


def test_get_total_ignores_missing_items():
    costs = {"socks": 5}
    items = ["socks", "shoes"]

    assert get_total(costs, items, 0.0) == 5.0
