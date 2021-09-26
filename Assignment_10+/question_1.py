def make_new_row(prev_row):
    """
    This function will construct the next row of pascals triangle

    This will be achieved by first making the edges which are always 
    1 and then looping through the previous row until the second to last
    one and constructing item by adding prev_row[index] + prev_row[index+1]
    This follows the logic of pascals triangle as the item beneath row will always
    be the product of 2 numbers that are above it.
    """
    if(len(prev_row) == 0):
        return [1]
    elif(len(prev_row) == 1):
        return [1, 1]
    else:
        counter = 0
        new_row = [1]
        for x in range(len(prev_row)-1):
            new_row.append(prev_row[x]+prev_row[x+1])
        new_row.append(1)
        return new_row

# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)
