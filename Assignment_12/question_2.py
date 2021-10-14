def main():
    file_name = input("Enter a filename: ")
    file_obj = open(file_name, "r")
    numbers = get_numbers_from_file(file_obj)
    print(sorted(numbers))


# The function get_numbers_from_file should be declared here
def get_numbers_from_file(file_obj):
    lines = file_obj.readlines()

    numbers = [int(lines[0].split(" ")[2])]
    for number_string in lines[1].split(","):
        number_string = number_string.strip()
        number = number_string.split(" ")[0]

        numbers.append(int(number))

    return numbers
    



if __name__ == "__main__":
    main()