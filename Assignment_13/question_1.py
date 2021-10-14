import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

YES = "y"
NO = "n"

def main():
    """
        This functin is the main program.
    """
    GAME_SEED = int(input("Input seed: "))
    random.seed(GAME_SEED)

    continue_play = YES
    while(continue_play == YES):
        play()

        continue_play = input("Play again (y/n): ")

def play():
    """
        This function is holds the game loop and initializes a new game.
    """
    victory = False
    row = 1
    col = 1
    coins = 0
    prev_tiles = []
    moves = 0

    while not victory:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row = play_one_move(col, row, valid_directions)

        if(is_coin_tile(col, row) and [col, row] != prev_tiles):
            if(pull_lever_input()):
                coins += 1
                print(f"You received 1 coin, your total is now {coins}.")
        
        moves += 1
        prev_tiles = [col, row]

    print(f"Victory! Total coins {coins}. Moves {moves}.")

        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions


def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")



def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = random.choice([NORTH, EAST, SOUTH, WEST])
    direction = direction.lower()

    print(f"Direction: {direction}")
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)

        victory = is_victory(col, row)

    return victory, col, row


def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)

def is_coin_tile(col, row):
    """
        This function checks if tile is a coin tile.
    """
    coin_tiles = [
        [1, 2],
        [2, 2],
        [2, 3],
        [3, 2]
    ]

    return [col, row] in coin_tiles

def pull_lever_input():
    """
        This function asks the user if he wants to pull the lever.
    """
    pull_lever = random.choice([YES, NO])
    print(f"Pull a lever (y/n): {pull_lever}")

    if(pull_lever == YES):
        return 1
    else:
        return 0

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)


if __name__ == "__main__":
    main()