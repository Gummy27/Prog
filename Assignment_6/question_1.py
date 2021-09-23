a_str = input("Input a string: ")
char_to_count = input("Input a character to count: ")

# Complete the program below

for index in range(len(a_str)):
    if(a_str[index] == char_to_count):
        print(index)