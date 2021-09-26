# ...add your functions

def file_into_list(filename):
    """
    This function takes in a filename and then reads a file into a list.
    """
    with open(filename, "r") as file:
        return file.readlines()

# You can keep these lines
file_name_a = input("First file: ")
file_name_b = input("Second file: ")

# ...fill in the rest

file_a = file_into_list(file_name_a)
file_b = file_into_list(file_name_b)

counter = 0
# This while loop will run until the counter has surpassed both lengths.
while(not(counter > len(file_a) and counter > len(file_b))):
    if(counter < len(file_a)):
        print(file_a[counter].strip())
    if(counter < len(file_b)):
        print(file_b[counter].strip())
    counter += 1
