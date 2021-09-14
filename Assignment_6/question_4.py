a_str = input("Enter a string: ")

# Complete the program below

for letter in a_str:
    if(letter.isupper()):
        print(letter.lower(), end="")
    else:
        print(letter.upper(), end="")