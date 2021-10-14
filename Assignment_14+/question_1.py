import csv

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

Then the program prints out the identified indices (nicely formatted),
to show an example of what can be done with the results.
"""

# https://stackoverflow.com/questions/6088581/what-are-python-best-practices-for-dictionary-dict-key-constants
FIRST_NAME = "First name"
LAST_NAME = "Last name"
EMAIL = "Email"
SECTION = "Section"

QUIZZES = "Quizzes"
ASSIGNMENTS = "Assignments"
EXTRA_ASSIGNMENTS = "Extra assignments"
PROJECTS = "Projects"
MIDTERMS = "Midterms"
FINAL_EXAM = "Final exam"

HEADERS = {
    "Quiz":QUIZZES, 
    "Assignment+":EXTRA_ASSIGNMENTS,
    "Assignment":ASSIGNMENTS,
    "Project":PROJECTS,
    "Midterm":MIDTERMS,
    "Final exam":FINAL_EXAM
}

COURSEWORK_COUNTER = 0
COURSEWORK_VALUE   = 1
# Feel free to change the values of these constants as you see fit



def main():
    filename = input("Enter filename: ")
    file_list = open_file(filename)
    if(file_list != None):
        student_dict = list_into_dict(file_list)
        # Implement your solution
        display_results(student_dict) # Feel free to change this line

# Feel free to add your own functions of course.

def open_file(filename) -> list:
    """
        This function will open the file using the csv library and return
        a list of words.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return list(csv.reader(file, delimiter=","))[0]
    except:
        print(f"File '{filename}' not found")
        return None

def list_into_dict(file_list) -> dict:
    """
        This function will take in a list of words and sort them into 
        coursework. Coursework that isn't recognized will be ignored.
    """
    student_dict = initialize_student_dict(file_list)
    counter = 4

    for coursework in file_list[4:]:
        header = isolate_header(coursework)

        for dict_header in HEADERS:
            if dict_header in header:
                student_dict[HEADERS[dict_header]].append([counter, coursework])
                break
        counter += 1
    
    return student_dict

def isolate_header(coursework) -> str:
    """
        This functino will take in the assignment description and isolate
        the header so that we can sort it accurately. 
    """
    header = coursework.split(":")[0]

    if("Final exam" in header):
        return header

    try:
        """
            This part is for the extra assignments as the only difference between
            it and regular assignments is the + symbol. So we take out the number
            and put the + symbol right after assignment.
        """

        header, number = header.split(" ")

        return header + "+"*number.count("+")

    except ValueError:
        return header

def initialize_student_dict(file_list) -> dict:
    """
        This function initializes the student dict so we don't have to use
        bulky try and except blocks.
    """
    student_dict = {}

    student_dict[FIRST_NAME] = [0, file_list[0]]
    student_dict[LAST_NAME]  = [1, file_list[1]]
    student_dict[EMAIL]      = [2, file_list[2]]
    student_dict[SECTION]    = [3, file_list[3]]

    student_dict[QUIZZES]            = []
    student_dict[ASSIGNMENTS ]       = []
    student_dict[EXTRA_ASSIGNMENTS ] = []
    student_dict[PROJECTS]           = []
    student_dict[MIDTERMS]           = []
    student_dict[FINAL_EXAM]         = []

    return student_dict

# You can make use of this function, but you need to make some fixes to get the output right.
# Feel free to change it as you see fit (including name and parameters).
def display_results(student_dict) -> None:
    """Prints out the identified indices along with the corresponding headers."""
    INDENT_ALIGN = 4

    print()

    for attribute in [FIRST_NAME, LAST_NAME, EMAIL, SECTION]:
        index = student_dict[attribute][COURSEWORK_COUNTER] # Where did you store the index of the column for this attribute?
        label = student_dict[attribute][COURSEWORK_VALUE]
        print(f"{index}: {label}")
    
    for category in [QUIZZES, ASSIGNMENTS, EXTRA_ASSIGNMENTS, PROJECTS, MIDTERMS]:
        header = category
        print(header+":")
        for coursework in student_dict[category]: # What do you need to iterate over to find what you're looking for?
            index = coursework[COURSEWORK_COUNTER] # Where did you store the index for this coursework?
            coursework_description = coursework[COURSEWORK_VALUE]
            print(f"{index:>{INDENT_ALIGN}}: {coursework_description}")
    
    if(student_dict[FINAL_EXAM]): # How can you see if the final exam was found in the file?
        index = student_dict[FINAL_EXAM][0][COURSEWORK_COUNTER] # Where did you store the index of the column for the final exam?
        label = student_dict[FINAL_EXAM][0][COURSEWORK_VALUE]
        print(f"{index}: {label}")
    else:
        print("The results from the final exam are not in yet.")


if __name__ == "__main__":
    main()
