def main():
    # Do not change this function,
    # or add anything to it
    filename_list = input("Enter filenames: ").split()
    process_all_files(filename_list)


# Add functions here below as required
def process_file_lines_into_list(lines):
    """
        This function takes in the lines from the data file and turns it into 
        a 2d matrix. It will filter out empty values and handle invalid values.
    """

    data_matrix = []
    for line in lines:
        temp = []
        for index, x in enumerate(line.strip().split(" ")):
            if(x):
                try:
                    temp.append(float(x))
                except:
                    if(index == 0):
                        temp.append(x)
                    else:
                        temp.append(0.00)
        data_matrix.append(temp)
    return data_matrix


def calculate_averages(data_matrix):
    """
        This function takes in the data and calculates the weight and 
        height average. This function will return a list that includes
        the name so it can be directly fed into the print function.
    """
    avg_weight, avg_height = 0, 0
    len_weight, len_height = 0, 0
    for item in data_matrix:
        if(item[1]):
            avg_weight += float(item[1])
            len_weight += 1
        if(item[2]):
            avg_height += float(item[2])
            len_height += 1
    return ["Average", avg_weight/len_weight, avg_height/len_height]

def insert_into_columns(data):
    """
        This function takes in a line of data and inserts it into columns with
        nice spacing.    
    """
    data[1] = f"{round(float(data[1]), 2):.2f}"
    data[2] = f"{round(float(data[2]), 2):.2f}"

    first_column = 12  - len(data[0])
    second_column = 10 - len(str(data[1]))
    third_column = 10  - len(str(data[2]))

    finished_columns =  data[0] + ' '*first_column
    finished_columns += ' '*second_column + data[1]
    finished_columns += ' '*third_column + data[2]
    
    return finished_columns

def print_out_information(filename, data_matrix, averages):
    """
        This function will print out the 2d matrix.
    """
    print(f"\nFile {filename}:")
    print(insert_into_columns(averages))
    print()
    for x in data_matrix:
        print(insert_into_columns(x))

def file_not_found(filename):
    """
        This function prints out a file not found error for the user.
    """
    print(f"\nFile {filename} not found")

def process_all_files(filename_list):
    """
        This function processes all the files into matrices and feeds it into 
        print out information.
    """

    for filename in filename_list:
        try:
            with open(filename, "r") as file:
                data_matrix = process_file_lines_into_list(file.readlines())
                averages = calculate_averages(data_matrix)
                print_out_information(filename, data_matrix, averages)
        except FileNotFoundError:
            file_not_found(filename)
            



# Main program starts here.
# Do not change or remove anything below this.
if __name__ == "__main__":
    main()