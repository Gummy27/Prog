def file_line_into_tuple(line):
    """
        This function will take in a file line and process it into
        a tuple.
    """
    formatted_data = ["", []]
    line = line.split(" ")

    for x in range(len(line)):
        if(x == 0):
            formatted_data[0] = line[x]
        else:
            try:
                formatted_data[1].append(int(line[x]))
            except:
                pass

    return tuple(formatted_data)

def read_project_file():
    """
        This function will read in project file name and then read 
        the file. It will then return the data processed.
    """
    filename = input("Project file name: ")
    with open(filename, "r") as file:
        project = file_line_into_tuple(file.readline())
    
    print(project)
    return project

def read_student_file():
    """
        This function will read in the students file name and then
        read the file. It ill the return the data processed into a 
        list.
    """
    filename = input("Students file name: ")

    with open(filename, "r") as file:
        students = []
        for line in file.readlines():
            students.append(file_line_into_tuple(line))
    print(students)
    return students



def calculate_grades(project, students):
    """
        This function will calculate the grade of each individual student
        and save it into a new tuple.
    """
    max_points = sum(project[1])

    new_students = []
    for student in students:
        temp = list(student)

        grade =  sum(temp[1]) / max_points * 10

        temp.append(grade)

        new_students.append(tuple(temp))

    print(new_students)
    return new_students

def format_line(line, header=False):
    """
        This function will format the data into neatly spaced out columns.
    """
    if(header):
        formatted_grade = "10.00"
    else:
        formatted_grade = f"{line[-1]:.2f}"

    first_column_spacing = " "*(20 - len(line[0]))
    second_column_spacing = " " * (5-len(formatted_grade))

    formatted_line = line[0] + first_column_spacing + " | "

    for x in line[1]:
        formatted_line += str(x) + " | "

    formatted_line += second_column_spacing + formatted_grade

    return formatted_line

def print_out_all_data(project, students):
    """
        This function will print everything out.
    """
    print(format_line(project, True))
    
    for x in students:
        print(format_line(x))

def user_input():
    try:
        project = read_project_file()
        students = read_student_file()
    except FileNotFoundError:
        print("Invalid file name")
        project, students = None, None


    return project, students

project, students = user_input()

if(project and students):
    students = calculate_grades(project, students)

    print_out_all_data(project, students)