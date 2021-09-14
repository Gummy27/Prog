a_str = input("Enter a string: ")
word_in_str = input("Enter in a substring you want to replace: ")
replacement = input("Enter in a substring you want to replace it with: ")

# Complete the program below
substring_is_in_string = False
# The for loop will check every position that the word_in_str fits
# to prevent overflow.
for index in range(len(a_str) - len(word_in_str), -1, -1):
    # Checks a_str from index to the length of word_in_str.
    if(a_str[index:index+len(word_in_str)] == word_in_str):
        a_str = a_str[:index] + replacement + a_str[index+len(word_in_str):]
        substring_is_in_string = True

if(substring_is_in_string):
    print(a_str)
elif(a_str == word_in_str):
    print(replacement)
else:
    print("Substring is not in the string")
