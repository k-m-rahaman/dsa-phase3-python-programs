class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.value/x.weight, reverse=True)

    total = 0

    for item in items:
        if capacity >= item.weight:
            total += item.value
            capacity -= item.weight

        else:
            total += item.value * (capacity / item.weight)
            break

    return total


items = [
    Item(60,10),
    Item(100,20),
    Item(120,30)
]

print(fractional_knapsack(items, 50))