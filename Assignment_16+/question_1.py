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
    filename = input("Enter filename: ")
    # Implement your solution
    # if something - what?
    # print(f"File '{filename}' not found")
    file_data = read_grades_from_file(filename)
    if(file_data):
        assignments_dict = build_assignment_dict(file_data)
        # print(project_dict)
        display_max_points(assignments_dict)  # Feel free to change this line
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
    assignments_dict = {}
    for header, value in zip(file_data[0], file_data[1]):
        category = determine_category(header)
        if category != "Unknown":
            if(category in [FIRST_NAME, LAST_NAME, EMAIL, SECTION]):
                assignments_dict[category] = value
            else:
                if(category in assignments_dict):
                    assignments_dict[category].append([header, value])
                else:
                    assignments_dict[category] = [[header, value]]
    return assignments_dict

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


if __name__ == "__main__":
    main()
