def convert_text_to_2d_matrix(text):
    text = text.split("\n")

    largest_len = 0
    for line in text:
        if(len(line) > largest_len):
            largest_len = len(line)

    text_2d_matrix = []
    for line in text:
        text_1d_matrix = []
        for letter in line:
            text_1d_matrix.append(letter)

        '''
            So everything is rotated correctly wee need to represent all spaces.
            Even those who come after the word.
        '''
        missing_spaces = largest_len - len(line)
        text_1d_matrix += ([" "]*missing_spaces)

        text_2d_matrix.append(text_1d_matrix)

    return text_2d_matrix

def rotate_text_clockwise(text):
    """ Rotates text 90 degrees clockwise, adding spaces as needed for multi-line strings """

    """ Convert the multiline string to a 2d matrix. This is so we can easily index the string. """
    text_2d_matrix = convert_text_to_2d_matrix(text)

    """
        This for loop is set up that it will print out the x-th letter in y-th array in the matrix.
        This rotating it 90 degrees.

        f.x.

        (1) 2 3     It will print out the first row in reverse order and all the subsequent rows.
        (4) 5 6     
        (7) 8 9
    """

    rotated_string = ""
    for x in range(len(text_2d_matrix[0])):
        for y in range(len(text_2d_matrix), 0, -1):
            rotated_string += text_2d_matrix[y-1][x]
        if(x != len(range(len(text_2d_matrix[0])))-1):
            rotated_string += "\n"

    return rotated_string
original = "Single line"
print(rotate_text_clockwise(original))
print("s\ni\nn\ng\nl\ne\n \nl\ni\nn\ne")