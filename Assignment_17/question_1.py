class WaterBottle:
    def __init__(self, max_capacity:int = 2, volume:int = 0) -> None:
        self.max_capacity = max_capacity
        self.volume = volume

    def __str__(self) -> str:
        return f"{self.volume:.1f}L"

    def fill(self):
        self.volume = self.max_capacity

    def drink(self, amount):
        if(amount > 0):
            if(self.volume >= amount):
                self.volume -= amount
            else:
                self.volume = 0
