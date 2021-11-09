# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid

def print_grid(grid) -> list:
    """
        The grid is printed out.
    """
    for line in grid:
        print(' '.join(line)+' ')
    print()

def move_into_cords(x: int, y: int, user_move: str) -> list:
    """
        This function is a series of if statements that will move 
        the player. 
    """
    if user_move == LEFT:
        x -= 1
    elif user_move == RIGHT:
        x += 1
    elif user_move == UP:
        y -= 1
    elif user_move == DOWN:
        y += 1
    
    if x < 0:
        return 4, y
    elif x > 4:
        return 0, y
    elif y < 0:
        return x, 4
    elif y > 4:
        return x, 0
    return x, y

def main():
    grid = initialize_grid()

    x, y = 0, 0
    print_grid(grid)
    user_move = get_move()
    while user_move != "q":
        grid[y][x] = EMPTY
        
        x, y = move_into_cords(x, y, user_move)

        grid[y][x] = POSITION

        print_grid(grid)

        user_move = input("Move: ")

if __name__ == "__main__":
    main()