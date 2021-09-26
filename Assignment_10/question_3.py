a_str = input("Enter a string: ")
list_of_indexes = input("Enter indices seperated by space: ").split()

# Main functionality goes here

def main():
    # Finish the function
    for index in list_of_indexes:
        try:
            print(f"{index}: {a_str[int(index)]}")
        except:
            pass

if __name__ == "__main__":
    main()