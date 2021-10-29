class ComplexNumber:
    def __init__(self, real_part: int = 0, complex_part: int = 0) -> None:
        self.real_part = real_part
        self.complex_part = complex_part

    def __str__(self) -> str:
        return f"{self.real_part}+{self.complex_part}i"

    def __add__(self, other : object) -> object:
        real_part = self.real_part + other.real_part
        complex_part = self.complex_part + other.complex_part

        return ComplexNumber(real_part, complex_part)

    def __sub__(self, other : object) -> object:
        real_part = self.real_part - other.real_part
        complex_part = self.complex_part - other.complex_part

        return ComplexNumber(real_part, complex_part)
    
    def __mul__(self, other : object) -> object:
        real_part = self.real_part * other.real_part - self.complex_part * other.complex_part
        complex_part = self.real_part * other.complex_part + other.real_part * self.complex_part

        return ComplexNumber(real_part, complex_part)

cmplx = ComplexNumber(20, 4)
cmplx2 = ComplexNumber(2, 3)
print(cmplx)
print(cmplx2)
print()
print(cmplx + cmplx2)
print(cmplx - cmplx2)
print(cmplx * cmplx2)