def construct_choice_string(viable_directions):
    '''
        This function will construct the choice string that the player sees.
    '''

    '''
        The directions are stored as a single letter but we want to print out
        the whole word. So we use a dict to connect the two for easy to read
        code.
    '''
    directions_dict = {
        "N" : "(N)orth",
        "S" : "(S)outh",
        "W" : "(W)est",
        "E" : "(E)ast"
    }
    choice_string = "You can travel: "

    for x in range(len(viable_directions)):
        '''
            We have to have a different output for the last direction so we don't
            print out or in the end of the sentence.
        '''
        if x == len(viable_directions)-1:
            choice_string += directions_dict[viable_directions[x]] + "."
        else:
            choice_string += directions_dict[viable_directions[x]] + " or "

    print(choice_string)

'''
We will store the map in a 2d array which closely resembles the original map.
In each tile is stored the viable directions you can go.
'''
tile_map = [
    ["N", "N", "N"],
    ["NES", "SW", "NS"],
    ["ES", "EW", "SW"]
    ]

cords_x, cords_y = 0, 0

while(not (cords_x == 2 and cords_y == 0)):
    construct_choice_string(tile_map[cords_y][cords_x])
    direction = input("Direction: ").upper()

    if(direction not in tile_map[cords_y][cords_x]):
        print("Not a valid direction!")

    elif(direction == "N"):
        cords_y += 1
    elif(direction == "S"):
        cords_y -= 1


    elif(direction == "E"):
        cords_x += 1
    elif(direction == "W"):
        cords_x -= 1
print("Victory!")