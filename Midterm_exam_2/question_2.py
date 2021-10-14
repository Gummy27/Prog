def main(): 
    file_name = input("Enter filename: ")
    file_stream = open_file(file_name)
    if file_stream is not None:
        file_data = readlines_to_list(file_stream)

        print_out_file_data_info(file_data)


        user_remove_punctuation = input("Remove punctuation (y/n)?: ")
        if(user_remove_punctuation == "y"):
            no_punct = remove_punctuation(file_data)

            print_out_file_data_info(no_punct)


        adjective = input("Enter an adjective (positive form): ")
        if(user_remove_punctuation == "y"):
            adjective_forms_in_file(adjective, no_punct)
        else:
            adjective_forms_in_file(adjective, file_data)

    else:
        print("File {} not found!".format(file_name))

# Your functions appear here

def open_file(filename):
    """
        This function opens the file and returns it read.
    """
    try:
        with open(filename, "r") as file:
            return file.read()
    except:
        return None

def readlines_to_list(file_data):
    """
        This function erases all newlines and splits the data into a list. It also 
        lowers all characters.
    """
    file_data_list = file_data.replace("\n", " ")

    file_data_list = file_data_list.split(" ")

    for index in range(len(file_data_list)):
        file_data_list[index] = file_data_list[index].lower()

    return file_data_list

def print_out_file_data_info(file_list):
    """
        This function prints out how many words were found and the raw list.
    """
    print(file_list)
    print(f"Found {len(file_list)} words")


def remove_punctuation(file_list):
    """
        This function removes punctuation from words. If words are all punctuation they
        are deleted.
    """
    new_list = []
    for word in file_list:
        new_word = ""
        for letter in word:
            if(letter.isalnum()):
                new_word += letter
        if(new_word):
            new_list.append(new_word)

    return new_list

def adjective_forms_in_file(adjective, file_data):
    """
        This function checks if all forms of a specific adjective is in file.
        It will print out all the forms that were found.
    """
    found_adjectives = ["", "", ""]
    forms = ["", "er", "est"]

    for index in range(len(forms)):
        if(adjective + forms[index] in file_data):
            found_adjectives[index] = adjective + forms[index]

    print(tuple(found_adjectives))
    
# Main program starts here
if __name__ == "__main__":
    main()