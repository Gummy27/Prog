def longest_line_in_array(array):
    """
        Finds the largest line in the array.
    """
    largest_len = 0

    for line in array:
        largest_len = max(len(line), largest_len)

    return largest_len

def smallest_indent_in_array(array):
    """
        Finds the longest indent in the array
    """
    smallest_indent = 0
    for line in array:
        temp = 0
        for letter in line:
            if(letter == " "):
                temp += 1
            else:
                break
        if(smallest_indent != 0):
            smallest_indent = min(smallest_indent, temp)
        else:
            smallest_indent = temp
    return smallest_indent
                


def change_indentation(text, spaces):
    """
    Adds or removes leading spaces to/from every line in the supplied string.

    A negative number of spaces instructs the function to remove spaces.
    A positive number of spaces instructs the function to add spaces.
    This function will automatically adjust the number of spaces to ensure that no line exceeds 80 characters.
    For example, if there's a line that's 78 characters long, and spaces = 4, then the function will only add
    2 spaces to each line.
    Similarily, it will not remove more spaces than it can. If one line has only 2 leading spaces and spaces = -4,
    then the function will remove exactly 2 spaces from each line.
    """
    # ... now add your code

    changed_text = text.split("\n")
    new_text = ""

    if(spaces > 0):

        largest_len = longest_line_in_array(changed_text)

        if(largest_len + spaces > 80):
            spaces = 80 - largest_len
        
        for x in range(len(changed_text)):
            if(x == len(changed_text)-1):
                new_text += " "*spaces + changed_text[x]
            else:
                new_text += " "*spaces + changed_text[x] + "\n"

        return new_text
    
    elif(spaces < 0):
        spaces *= -1
        smallest_indent = smallest_indent_in_array(changed_text)
        if(smallest_indent - spaces < 0):
            spaces = smallest_indent
        
        for index in range(len(changed_text)):
            if(index == len(changed_text)-1):
                new_text += changed_text[index].replace(" ", "", spaces)
            else:
                new_text += changed_text[index].replace(" ", "", spaces) + "\n"
        
        return new_text

    else:
        return text

original = "print(x)\ny = input()"

expected = "    print(x)\n    y = input()"

actual = change_indentation(original, 4)

print(actual)
print(expected)

assert actual == expected