class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"|{self.x}|\n|{self.y}|\n"

    def add(self, other):
        self.x += other.x
        self.y += other.y
    
    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
    
    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar

vec1 = Vector2D(1, 1)
print(vec1)

vec2 = Vector2D(2,2)
print(vec2)

vec3 = Vector2D(3,3)
print(vec3)

vec1.add(vec2)
print(vec1)

vec3.subtract(vec2)
print(vec3)

vec2.scale(5)
print(vec2)