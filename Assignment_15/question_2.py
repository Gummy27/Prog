def main():
    filename1 = input("Enter the path to the first file: ")
    filename2 = input("Enter the path to the second file: ")

    data = read_multiple_files([filename1, filename2])
    if(data != None):
        set1, set2 = map(set, data)

        and_set       = set1.intersection(set2)
        xor_set       = set1.symmetric_difference(set2)
        only_file_one = set1.intersection(xor_set)

        print(f"The two files have {len(and_set)} words in common.")
        print(f"These words are as follows: {set_to_string(and_set)}.")

        print(f"There are {len(xor_set)} words that are only in either file but not both.")
        print(f"These words are as follows: {set_to_string(xor_set)}.")

        print(f"There are {len(only_file_one)} words that only appear in the first file.")
        print(f"These words are as follows: {set_to_string(only_file_one)}.")

def read_multiple_files(filenames: list) -> list:
    """
        This function takes in multiple filenames and returns
        the data of these file split by " ".
    """
    try:
        file_data = []
        for filename in filenames:
            with open(filename, "r") as file:
                file_data.append(file.read().split())
        return file_data
    except FileNotFoundError:
        return None

def set_to_string(set_data) -> str:
    """
        This function takes in a set and formats it into
        string with commas and and seperating the words.
    """
    set_sorted_list = list(sorted(set_data))

    set_string = ""
    for index in range(len(set_sorted_list)):
        if(index == len(set_sorted_list)-1):
            set_string += "and " + set_sorted_list[index]
        else:
            set_string += set_sorted_list[index] + ", "
    return set_string





if __name__ == "__main__":
    main()