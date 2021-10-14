def main():
    # Finish the function
    user_continue = "y"
    my_dict = {}

    while(user_continue == "y"):
        word = input("Input a word: ")
        definition = input(f"Enter the definition for {word}: ")

        my_dict[word] = definition

        user_continue = input("Would you like to add another word and definition (y/n)?: ")

    my_list = []
    for key in my_dict:
        my_list.append((key, my_dict[key]))

    print(sorted(my_list))

if __name__ == "__main__":
    main()