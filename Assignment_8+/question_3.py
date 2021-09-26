def print_out_matrix(matrix, indent):
    """
        This function will print out the matrix cleanly.
    """

    for array in matrix:
        if(max(array) != " "):
            print(" "*indent, end="")
            for letter in array:
                print(letter, end="")
            print("")


def rotate_text_clockwise(matrix):
    """
        This function will rotate the matrix by looping through
        the indexes and flipping them. This will end in a 90 deg
        rotation.
    """

    rotated_matrix = []
    for x in range(len(matrix)):
        temp = []
        for y in range(len(matrix[x]), 0, -1):
            temp.append(matrix[y-1][x])
        rotated_matrix.append(temp)

    return rotated_matrix


def change_indentation(indent, addition):
    """
        This function will check if the indent is legal and then
        return the computed indent.
    """
    if(indent + addition > 0):
        return indent + addition
    else:
        return indent

"""
I will use a matrix to store the piece as it is the most 
intuitive and easily understood method.
"""
piece_matrix = [
    [" ", " ", " "],
    ["X", " ", " "],
    ["X", "X", "X"]
]
indent = 0

command = ""
while(command != "q"):
    command = input("(r)ight, (l)eft, (t)urn, (q)uit: ")

    if(command == "r"):
        indent = change_indentation(indent, 1)
    elif(command == "l"):
        indent = change_indentation(indent, -1)
    elif(command == "t"):
        piece_matrix = rotate_text_clockwise(piece_matrix)
    
    if(command != "q"):
        print_out_matrix(piece_matrix, indent)
    