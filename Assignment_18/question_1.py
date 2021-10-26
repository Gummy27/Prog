class Pair:
    def __init__(self, val1: int = 0, val2: int = 0) -> None:
        self.val1 = val1
        self.val2 = val2

    def __str__(self) -> str:
        return f"Value 1: {self.val1}, Value 2: {self.val2}"

    def __add__(self, other):
        val1 = self.val1 + other.val1
        val2 = self.val2 + other.val2

        return Pair(val1, val2)

    def __mul__(self, other):
        val1 = self.val1 * other.val1
        val2 = self.val2 * other.val2

        return Pair(val1, val2)

pair1 = Pair(20,30)
print(pair1)
pair2 = Pair(40,50)
pair3 = pair1 + pair2
print(pair3)
pair4 = pair1 * pair2
print(pair4)