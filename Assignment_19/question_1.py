class Student:
    def __init__(self, id: int, grades: list) -> None:
        self.id = id
        self.grades = grades

    def __str__(self) -> str:
        return_string = f"Student ID: {self.id}"
        return_string += f"\nGrades: {self.grades}"
        return return_string
    
    def __lt__(self, other: object) -> bool:
        return self.avg_grade() < other.avg_grade()

    def avg_grade(self) -> float:
        return sum(self.grades) / len(self.grades)

    def get_max_grade(self) -> float:
        return max(self.grades)

student1 = Student(1, [3.0, 4.6, 3.4, 5.4])
student2 = Student(2, [9.5, 9.0, 8.9, 9.8])