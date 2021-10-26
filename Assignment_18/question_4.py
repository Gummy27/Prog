class BackpackItem:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f"BackpackItem({self.name}, {self.weight})"

class Backpack:
    def __init__(self, weight_limit):
        self.weight_limit = weight_limit
        self.current_weight = 0
        self.items = []

    def __str__(self) -> str:
        return f"Backpack({self.current_weight}/{self.weight_limit}): {self.items}"

    def add(self, item : BackpackItem) -> None:
        if item.weight + self.current_weight <= self.weight_limit:
            self.current_weight += item.weight
            self.items.append(item)
        else:
            print("Maximum capacity would be exceeded!")

bp = Backpack(10)
print(bp)
bp.add(BackpackItem("Book", 7))
print(bp)
bp.add(BackpackItem("Laptop", 3))
print(bp)
bp.add(BackpackItem("Headphones", 2))
print(bp)