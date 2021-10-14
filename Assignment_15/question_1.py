def main():
    word_set = set()

    user_input = input("Enter a word to add to the set: ")
    while(user_input != "q"):
        word_set.add(user_input)
        print_ordered_set(word_set)
        print(f"The size of the set is: {len(word_set)}")
        user_input = input("Enter a word to add to the set: ")

def print_ordered_set(word_set: set) -> None:
    """
        This will print out the set in order.
    """
    for x in sorted(word_set):
        print(x, end=" ")
    print()

if __name__ == "__main__":
    main()