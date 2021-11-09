COUNTER = 0
PASSWORD_LENGTH = 1
DIGIT_COUNTER = 2
PASSWORD_LIST = 3

INVALID = 0
VALID = 1

def main():

    """
        This list will store all information about the passwords that were entered.
        It has a list for valid passwords and invalid passwords. A number of constants
        are used to index the list. 
    """
    password_info = [
        [0, 0, 0, []],
        [0, 0, 0, []]
    ]

    password = get_user_input()
    while password != "quit":
        valid_bool = password_validity(password)
        
        print_validity_of_password(valid_bool)
        password_info = write_password_info(password, password_info, valid_bool)

        password = get_user_input()
    
    print_out_password_info(password_info)


def get_user_input() -> str:
    """
        This function will take in user input and return it.
    """
    return input("Enter password: ")

def count_digits(string: str) -> int:
    """
        This function counts the number of digits in a string.
    """
    digit_counter = 0

    for letter in string:
        try: 
            int(letter)
            digit_counter += 1
        except:
            pass
    
    return digit_counter

def password_validity(password: int) -> bool:
    """
        This function checks if the password is valid. It consists of 2 flags.

        flag 1: Checks if Password has at least 3 digits.

        flag 2: Checks if Password is at least 8 letters long.
    """
    digit_counter = count_digits(password)

    flag_1 = digit_counter >= 3
    flag_2 = len(password) >= 8

    return flag_1 and flag_2

def print_validity_of_password(valid: bool) -> None:
    """
        This function prints out if the password is valid or not.
    """
    if valid:
        print("Password is valid")
    else:
        print("Password is invalid")

def write_password_info(password: str, password_info: list, valid_invalid: bool) -> list:
    """
        This function writes password information to the password information list. 
    """
    password_info[valid_invalid][COUNTER] += 1
    password_info[valid_invalid][PASSWORD_LENGTH] += len(password)
    password_info[valid_invalid][DIGIT_COUNTER] += count_digits(password)
    password_info[valid_invalid][PASSWORD_LIST].append(password)

    return password_info

def print_out_password_info(password_info: list) -> None:
    """
        This function prints out the password information list.
    """
    print()
    for valid_invalid in [VALID, INVALID]:
        active_password_info = password_info[valid_invalid]
        if active_password_info[COUNTER]:
            password_length_avg = active_password_info[PASSWORD_LENGTH] / active_password_info[COUNTER]
            password_nr_of_digits_avg = active_password_info[DIGIT_COUNTER] / active_password_info[COUNTER]

            if valid_invalid == VALID:
                print("Valid passwords:")
            else:
                print("Invalid passwords:")

            print(' '.join(active_password_info[PASSWORD_LIST]))
            print(f"Average length: {password_length_avg:.1f}")
            print(f"Average # of digits: {password_nr_of_digits_avg:.1f}")
            print()

# Main program starts here
if __name__ == "__main__":
    main()