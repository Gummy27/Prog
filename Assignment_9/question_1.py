# get_char_at_index function definition goes here
def get_char_at_index(string, index):
    """
    This function will find return a specific letter of string.
    """
    if(index < len(string)):
        return string[index]
    else:
        return None

def main():
    a_str = input("Enter a string: ")
    index = input("Enter an index: ")
    # Call your function here below


    try:
        index = int(index)
        
        char_at_index = get_char_at_index(a_str, index)

        if char_at_index: # If char_at_index is not None
            print(f"The character at index {index} is '{char_at_index}'.")
        else:
            print("Index out of range.")
    except ValueError:
        print("Index not an integer.")

if __name__ == "__main__":
    main()