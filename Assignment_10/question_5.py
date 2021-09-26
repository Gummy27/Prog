# Main functionality starts here, you may change anything you like
def main():
    left_side = ["w", "g", "c"]
    right_side = []
    is_left = True
    failed_game = False
    display_state(left_side, right_side, is_left)
    while len(left_side) and not failed_game:
        take_over = input("What would you like to take over the river? (w/g/c/e): ")

        if(take_over != "e"):
            if(is_left):
                left_side.pop(left_side.index(take_over))
                right_side.append(take_over)
            else:
                right_side.pop(right_side.index(take_over))
                left_side.append(take_over)

        is_left = not is_left
        display_state(left_side, right_side, is_left)
        failed_game = check_if_eaten([left_side, right_side][is_left])

    if(len(left_side) == 0):
        print("You solved the puzzle!")
# Add your functions here

def check_if_eaten(side):
    """
    This function takes in the side that the player is not on and
    checks if the user failed the game by leaving either the wolf and
    goat alone or the goat and the cabbage alone.
    """
    if("g" in side and "c" in side):
        print("The goat ate the cabbage.")
        return True
    elif("g" in side and "w" in side):
        print("The wolf ate the goat.")
        return True
    else:
        return False
    

def display_state(left_side, right_side, is_left):
    """
    This function will print out the state of the game.
    """
    if(is_left):
        print("You are on the left side.")
    else:
        print("You are on the right side.")
    print(" ".join(left_side), "|", " ".join(right_side))

if __name__ == "__main__":
    main()