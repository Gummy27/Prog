from abc import ABC, abstractmethod
from math import floor

class Canvas(ABC):
    @abstractmethod
    def draw_backslash(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_upper_left_corner(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_upper_right_corner(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_lower_left_corner(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_lower_right_corner(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_vertical_line(self, x: int, y: int, length: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_horizontal_line(self, x: int, y: int, length: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def set_color(self, color_index: int) -> None:
        raise NotImplementedError

# Add your shape classes below
class Shape:
    def __init__(self, x : int, y : int, width : int, height : int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, delta_x=0, delta_y=0):
        self.x += delta_x
        self.y += delta_y

class VerticalLine(Shape):
    def __init__(self, x: int, y: int, length: int) -> None:
        self.x = x
        self.y = y
        self.length = length
    
    def draw(self, canvas: Canvas):
        canvas.draw_vertical_line(self.x, self.y, self.length)
    
class HorizontalLine(Shape):
    def __init__(self, x: int, y: int, length: int) -> None:
        self.x = x
        self.y = y
        self.length = length
    
    def draw(self, canvas: Canvas):
        canvas.draw_horizontal_line(self.x, self.y, self.length)

class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y, width, height)

    def draw(self, canvas : Canvas) -> None:
        canvas.draw_upper_left_corner(self.x, self.y)
        canvas.draw_upper_right_corner(self.x + self.width - 1 , self.y)
        canvas.draw_lower_left_corner(self.x, self.y + self.height - 1)
        canvas.draw_lower_right_corner(self.x + self.width - 1, self.y + self.height - 1)

        if self.width > 2:
            canvas.draw_horizontal_line(self.x + 1, self.y, self.width - 2)
            canvas.draw_horizontal_line(self.x + 1, self.y + self.height - 1, self.width-2)

        if self.height > 2:
            canvas.draw_vertical_line(self.x, self.y + 1, self.height - 2)
            canvas.draw_vertical_line(self.x + self.width - 1, self.y + 1, self.height - 2)

class Square(Rectangle):
    def __init__(self, x: int, y: int, size: int) -> None:
        super().__init__(x, y, width=size, height=size)

class Triangle(Shape):
    def __init__(self, x: int, y: int, size: int) -> None:
        self.x = x
        self.y = y
        self.size = size

    def draw(self, canvas : Canvas) -> None:
        canvas.draw_lower_left_corner(self.x, self.y + self.size - 1)

        canvas.draw_horizontal_line(self.x + 1, self.y + self.size - 1, self.size - 1)

        canvas.draw_vertical_line(self.x, self.y, self.size-1)
        
        for offset in range(1, self.size - 1):
            canvas.draw_backslash(self.x + offset, self.y + offset)

