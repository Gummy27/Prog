class Square:
    def __init__(self, size = 1) -> None:
        if size <= 0 :
            size = 1
        self.__size =  size

    def area(self):
        return self.__size ** 2

    def perimeter(self):
        return self.__size * 4

    def __str__(self) -> str:
        return f"Side length: {self.__size}"

    def __eq__(self, other: object) -> bool:
        return self.area() == other.area()

    def __repr__(self) -> str:
        return f"Square({self.__size})"

sq1 = Square()
sq2 = Square(10)
print(sq1)
print(sq1.area())
print(sq1.perimeter())
print(sq1.__repr__())
print(sq1 == sq2)