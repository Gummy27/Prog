def main():
    # Finish the function
    user_continue = "y"
    my_dict = {}

    while(user_continue == "y"):
        email = input("Enter the student email: ")
        grade = int(input("Enter the students grade: "))

        my_dict = insert_into_dict(my_dict, email, grade)

        user_continue = input("Would you like to add another grade (y/n)?: ")
    
    print_out_dict(my_dict)


# Add your functions here
def insert_into_dict(my_dict, key, value):
    try:
        my_dict[key].append(value)
    except KeyError:
        my_dict[key] = [value]

    return my_dict

def print_out_dict(my_dict):
    for key, value in my_dict.items():
        print(f"{key}: {round(sum(value) / len(value), 2)}")

if __name__ == "__main__":
    main()