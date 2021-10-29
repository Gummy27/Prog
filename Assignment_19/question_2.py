class Shape:
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        return f"{type(self).__name__} with area of {self.get_area()} and perimeter of {self.get_perimeter()}"

class Rectangle(Shape):
    def __init__(self, length: int, height: int) -> None:
        self.length = length
        self.height = height

    def get_area(self) -> int:
        return self.length * self.height

    def get_perimeter(self) -> int:
        return self.length * 2 + self.height * 2

class Square(Rectangle):
    def __init__(self, length: int) -> None:
        super().__init__(length, length)

rect = Rectangle(2, 2)
print(rect.get_area())
print(rect.get_perimeter())
print(rect)

sq = Square(2)
print(sq.get_area())
print(sq.get_perimeter())
print(sq)