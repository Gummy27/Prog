def main():
    file_name = input("Enter a filename: ")
    file_obj = open_file(file_name)
    # Finish the rest of the function

    if(file_obj != None):
        len_dict = string_list_into_len_dict(file_obj)

        user_len = int(input("Enter the length you want to search for: "))

        print_dict_list(len_dict, user_len)

    else:
        print("Invalid file!")

# Your functions go here
def open_file(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except:
        return None

def string_list_into_len_dict(file_obj):
    len_dict = {}
    for string in file_obj:
        string = string.strip()

        try:
            len_dict[len(string)].append(string)
        except:
            len_dict[len(string)] = [string]

    return len_dict

def print_dict_list(my_dict, key):
    try:
        country_list = my_dict[key]
        
        for x in range(len(country_list)):
            if(x != len(country_list)-1):
                print(country_list[x], end=", ")
            else:
                print(country_list[x])
    except:
        print("No country name of length 2 exists.")

if __name__ == "__main__":
    main()