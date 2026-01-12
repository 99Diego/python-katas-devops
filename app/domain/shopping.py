def get_total(costs: dict, items: list, tax: float) -> float:
    total = 0

    for item in items:
        if item in costs:
            total += costs[item]

    total_with_tax = total * (1 + tax)
    return round(total_with_tax, 2)
