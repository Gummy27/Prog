"""A program that prepares to calculate final grades of students in this course.

Takes as input a .csv file exported from the gradebook on Mímir.
We need to extract information for every student on how many points they scored
in individual quizzes, assignments, projects and exams,
as well as the maximum available points for each.

Since not all of those have been performed in Mímir already,
it is unknown at this time in which order they will appear in the file.
So this program identifies the columns dynamically
(after the semester is over, it will be possible to simplify this program
by providing this mapping as hard-coded constants).

Next, it extracts information from the file, about the maximum available points for each coursework,
and prints it out (nicely formatted), to show an example of what can be done with the results.
"""

import csv


# https://stackoverflow.com/questions/6088581/what-are-python-best-practices-for-dictionary-dict-key-constants
FIRST_NAME = "First name"
LAST_NAME = "Last name"
EMAIL = "Email"
SECTION = "Section"

QUIZZES = "Quizzes"
QUIZZES_IND = "Individual quizzes"
QUIZZES_GROUP = "Group quizzes"
ASSIGNMENTS = "Assignments"
EXTRA_ASSIGNMENTS = "Extra assignments"
PROJECTS = "Projects"
MIDTERMS = "Midterms"
FINAL_EXAM = "Final exam"

UNIQUE_CATEGORIES = [FIRST_NAME, LAST_NAME, EMAIL, SECTION, FINAL_EXAM]
LIST_CATEGORIES = [
    QUIZZES_IND,
    QUIZZES_GROUP,
    ASSIGNMENTS,
    EXTRA_ASSIGNMENTS,
    PROJECTS,
    MIDTERMS,
]

HEADER_PREFIXES = {
    FIRST_NAME: "First Name",
    LAST_NAME: "Last Name",
    EMAIL: "Email",
    SECTION: "Section",
    QUIZZES: "Quiz",
    ASSIGNMENTS: "Assignment",
    PROJECTS: "Project",
    MIDTERMS: "Midterm",
    FINAL_EXAM: "Final",
}

ASSIGNMENT_NAME = 0
ASSIGNMENT_MAX_POINTS = 1

# Feel free to change the values of these constants as you see fit


def main():
    filename = "new_sample.txt" # input("Enter filename: ")
    # Implement your solution
    # if something - what?
    # print(f"File '{filename}' not found")
    file_data = read_grades_from_file(filename)
    if(file_data):
        students_dict, max_points_dict = build_assignment_dict(file_data)
        
        build_grade_dict(students_dict)
        # print(project_dict)
        # display_max_points(assignments_dict)  # Feel free to change this line
    else:
        print(f"File '{filename}' not found")


# You can use the following functions as provided, or for inspiration.
# Feel free to change them as you see fit.
def read_grades_from_file(filename: str) -> list:
    """Parses the file into a list of lists, one for each line of the file."""
    try:
        with open(filename, encoding="utf-8") as grade_file:
            return list(csv.reader(grade_file))

    except FileNotFoundError:
        return None


def build_assignment_dict(file_data):
    students_dict = []
    points_possible_dict = {}

    file_header = file_data[0]
    max_points = file_data[1]

    for student in file_data[1:]:
        assignments_dict = {}
        for header, value, max in zip(file_header, student, max_points):
            category = determine_category(header)
            if category != "Unknown":
                if(category in [FIRST_NAME, LAST_NAME, EMAIL, SECTION]):
                    assignments_dict[category] = value
                else:
                    grade_out_of_10 = round(float(value) / float(max) * 10, 2)
                    if(category in assignments_dict):
                        assignments_dict[category].append([header, grade_out_of_10])
                    else:
                        assignments_dict[category] = [[header, grade_out_of_10]]
        if(points_possible_dict == {}):
            points_possible_dict = assignments_dict
        else:
            students_dict.append(assignments_dict)

    return students_dict, points_possible_dict

def build_grade_dict(student_dict):
    for student in student_dict:
        quiz_grade = calculate_combined_quiz_grade(
            student[QUIZZES_IND], student[QUIZZES_GROUP]
        )
        print(student[FIRST_NAME], quiz_grade)
        assignments_grade = calculate_assignment_grade(student[ASSIGNMENTS])
        projects_grade = calculate_project_grade()
        exams_grade = calculate_exam_grade()

def identify_columns(headers_line: list) -> dict:
    """Figures out what the indices of various headers are.

    Args:
      headers_line:
        The first line of the gradebook, which contains the column headers.
        Will not be modified.

    Returns:
        A dictionary with the indices of all relevant headers.
        For example:

        {
            FIRST_NAME: 0,
            LAST_NAME: 1,
            EMAIL: 2,
            SECTION: 3,
            QUIZZES_IND: [4, 8, 16, 24],
            QUIZZES_GROUP: [6, 12, 20, 28],
            ASSIGNMENTS: [5, 9, 14, 17, 19, 26, 29, 32, 34],
            EXTRA_ASSIGNMENTS: [7, 10, 13, 18, 21, 25, 30],
            PROJECTS: [11, 15, 22, 27, 33],
            MIDTERMS: [23, 31],
            FINAL_EXAM: 35,
        }

        The intended use of this dictionary is demonstrated by the following examples:
        >>> columns = identify_columns(gradebook[0])
        Given a line from the gradebook for a particular student:

        1. The name of the student is found as:
        >>> name = f"{line[columns[FIRST_NAME]]} {line[columns[LAST_NAME]]}"

        2. Index of grade from final exam (which is unique):
        >>> final_exam_score = line[columns[FINAL_EXAM]]

        3. Index of grades from other categories, such as projects:
        >>> project_scores = [line[column] for column in columns[PROJECTS]]
    """

    columns = {}
    for category in LIST_CATEGORIES:
        columns[category] = []

    for index, header in enumerate(headers_line):
        category = determine_category(header)
        if category in LIST_CATEGORIES:
            columns[category].append(index)
        elif category in UNIQUE_CATEGORIES:
            columns[category] = index

    return columns


def determine_category(header: str) -> str:
    """Determines which category the given header belongs to."""

    # Special care must be taken to distinguish between the normal assignments and the extra assignments.
    # The header for assignment 1 begins with "Assignment 1:".
    # The header for assignment 1+ begins with "Assignment 1+:"
    # They share the prefix "Assignment 1"
    # so checking the header for the prefix "Assignment" is not enough to distinguish between these two categories.

    # Special care must also be taken to distinguish between
    # the individual quizzes and the group quizzes,
    # since they share a common prefix.
    # The header for the quizzes from lecture 1 begin with
    # "Quiz 1 (Individual):" and "Quiz 1 (Group):", for example.
    # So checking the header for the prefix "Quiz" is not enough to distinguish between them.

    for category in HEADER_PREFIXES:
        if header.startswith(HEADER_PREFIXES[category]):
            if category == ASSIGNMENTS and "+:" in header:
                return EXTRA_ASSIGNMENTS
            if category == QUIZZES:
                if "(Individual)" in header:
                    return QUIZZES_IND
                else:
                    assert "(Group)" in header
                    return QUIZZES_GROUP
            return category

    return "Unknown"


# Feel free to add more functions

# You can make use of this function, but you need to make some fixes to get the output right.
# Feel free to change it as you see fit (including name and parameters).
def display_max_points(assignments_dict) -> None:
    """Prints out the maximum available points for each coursework along with the corresponding headers."""
    DECIMAL_PLACES = 1
    INDENT_ALIGN = 5 + DECIMAL_PLACES

    print()

    for category in LIST_CATEGORIES:
        header = category
        print(f"{header}:")
        for assignment in assignments_dict[category]:  # What do you need to iterate over to find what you're looking for?
            max_points = float(assignment[ASSIGNMENT_MAX_POINTS])  # Where can you find the maximum points for this coursework? Did you store them somewhere?
            coursework = assignment[ASSIGNMENT_NAME]  # What should go here?
            print(
                f"{max_points:>{INDENT_ALIGN}.{DECIMAL_PLACES}f} points possible for {coursework}"
            )

    if FINAL_EXAM in assignments_dict:  # How can you see if the final exam was found in the file?
        max_points = float(assignments_dict[FINAL_EXAM][0][ASSIGNMENT_MAX_POINTS])  # Where can you find the maximum points for the final exam?
        label = assignments_dict[FINAL_EXAM][0][ASSIGNMENT_NAME]  # What does the header for the final exam look like in the file? Can you look it up?
        print(f"{max_points} points possible for {label}")
    else:
        print("The number of possible points on the final exam is not available yet.")

def calculate_combined_quiz_grade(
    individual_quiz_grades: list, group_quiz_grades: list
) -> float:
    """Calculates the contribution from the quiz grades toward the final grade.

    Follows the Assessment specification on Canvas:
    - Short quizzes in class: 10%  (75% best count).  Individual quizzes 5%, group quizzes 5%

    Calculates the grades separately for individual quizzes and group quizzes,
    then combines the two.

    Args:
      individual_quiz_grades:
        A list of a particular student's grades from individual quizzes.
        Will not be modified.
      group_quiz_grades:
        A list of a particular student's grades from group quizzes.
        Will not be modified.

    Returns:
        A single combined grade from the quizzes (both individual and group quizzes).
    """

    individual_grade = calculate_quiz_grade(individual_quiz_grades)
    group_grade      = calculate_quiz_grade(group_quiz_grades)

    return (individual_grade + group_grade) / 2



def calculate_quiz_grade(quiz_grades: list) -> float:
    """Calculates the contribution from the quiz grades toward the final grade.

    Follows the Assessment specification on Canvas:
    - Short quizzes in class: 10%  (75% best count).  Individual quizzes 5%, group quizzes 5%

    Drops the lowest quarter of grades, and averages the rest.

    Args:
      quiz_grades:
        A list of a particular student's quiz grades (for either individual or group quizzes).
        Will not be modified.

    Returns:
        A single combined grade from the given category of quizzes.
    """
    grades = [grades[1] for grades in quiz_grades]
    grades = sorted(grades)
    valid_grades = grades[int(len(grades)/4):]

    return round(sum(valid_grades) / len(valid_grades), 2)


def calculate_assignment_grade(
    assignment_grades: list, extra_assignment_grades: list
) -> float:
    """Calculates the contribution from the assignment grades toward the final grade.

    Follows the Assessment specification on Canvas:
    - Programming projects in class: 10% (Full points if the students gets 50%, on average, for these projects over the whole term)

    Calculates the average, and scales up by a factor of 2 (limited to full points)

    Args:
      assignment_grades:
        A list of a particular student's assignment grades.
        Will not be modified.
      extra_assignment_grades:
        A list of the same student's extra assignment grades.
        Will not be modified.

    Returns:
        A single combined grade from the assignments and the extra assignments.
    """

    grades = [grades[1] for grades in assignment_grades+]


def calculate_project_grade(project_grades: list) -> float:
    """Calculates the contribution from the project grades toward the final grade.

    Follows the Assessment specification on Canvas:
    - Homework/weekly projects (max group size 2): 20% (7 best of 11 count)

    Drops the lowest 4, and averages the remaining 7.

    Args:
      project_grades:
        A list of a particular student's project grades.
        Will not be modified.

    Returns:
        A single combined grade from the projects.
    """

    raise NotImplementedError  # remove this line and provide your implementation.


def calculate_exam_grade(midterm_grades: list, final_exam_grade: float) -> float:
    """Calculates the contribution from the grades from the midterm exams and final exam toward the final grade.

    Follows the Assessment specification on Canvas:
    - Midterm exams: 20%  (Two midterms, no repeat exam)
    - Final exam: 40-60%.  The grade of 5 is needed to pass the course.
    - If a student obtains a higher grade in the final exam compared to the midterm exams,
    - then the weight of the final exam is 60%, otherwise 40%.

    Each midterm grade contributes 10% to the final grade,
    but only those that are higher than the grade from the final exam.
    Those that are lower are ignored, and the final exam counts more instead.

    Args:
      midterm_grades:
        A list of a particular student's midterm grades.
        Will not be modified.
      final_exam_grade:
        The same student's final exam grade.

    Returns:
        A single combined grade from the midterms and the final exam.
    """

    raise NotImplementedError  # remove this line and provide your implementation.


def calculate_final_grade(
    quiz_grade: float, assignment_grade: float, project_grade: float, exam_grade: float
) -> float:
    """Calculates the final grade from the various contributing factors.

    Follows the Assessment specification on Canvas:
    - Short quizzes in class: 10%
    - Programming projects in class: 10%
    - Homework projects (max group size 2): 20%
    - Midterm exams: 20%
    - Final exam: 40-60%.
    - If a student obtains a higher grade in the final exam compared to the midterm exams,
    - then the weight of the final exam is 60%, otherwise 40%.

    Calculates the weighted average of the quizzes, class projects (assignments), homework projects and exams (miderms and final exam),
    with weights:
        10% - quizzes
        10% - assignments
        20% - projects
        60% - exams

    Args:
      quiz_grade:
        A single combined grade from the quizzes.
      assignment_grade:
        A single combined grade from the assignments and the extra assignments.
      project_grade:
        A single combined grade from the projects.
      exam_grade:
        A single combined grade from the midterms and the final exam.

    Returns:
        A single combined grade from the quizzes, assignments, projects and exams.
    """

    raise NotImplementedError  # remove this line and provide your implementation.


# You might find the following function useful.
# It contains the details necessary to get the form of the presentation correct,
# such as whitespace padding and so on.
def display_grades(student_dicts: list) -> None:
    """Prints out the top 10 student grades.

    Args:
      student_dicts:
        A list of dictionaries, one for each student, containing name and final grade,
        along with intermediate grades for each category.
        Will not be modified.
    """

    NAME_WIDTH = 35
    HEADER_WIDTH = 20
    RIGHT_ALIGN = 11
    DECIMAL_PLACES_INTERMEDIATE = 2
    DECIMAL_PLACES_FINAL = 1
    HORIZONTAL_SEPARATOR = "-" * 180

    descending = sorted(
        student_dicts, key=operator.itemgetter(FINAL_GRADE), reverse=True
    )
    top_ten = []
    # If only we had some way of getting a list of the top ten students. Hmm...

    print(f"\n{'Name':{NAME_WIDTH}}", end="")
    for header in [
        "Quizzes (10%)",
        "Assignments (10%)",
        "Projects (20%)",
        "Exam grade (60%)",  # Combined grade from midterms and final exam
        "Final grade (100%)",
    ]:
        print(f"{header:^{HEADER_WIDTH}}", end="")
    print()

    print(HORIZONTAL_SEPARATOR)
    for student in top_ten:
        print(f"{student[NAME]:{NAME_WIDTH}}", end="")
        for category in [QUIZZES, ASSIGNMENTS, PROJECTS, EXAM]:
            grade = student[f"{category}{GRADE}"]
            print(f"{10*grade:^{HEADER_WIDTH}.{DECIMAL_PLACES_INTERMEDIATE}f}", end="")
        print(f"{10*student[FINAL_GRADE]:>{RIGHT_ALIGN}.{DECIMAL_PLACES_FINAL}f}")
    print(HORIZONTAL_SEPARATOR)


if __name__ == "__main__":
    main()
