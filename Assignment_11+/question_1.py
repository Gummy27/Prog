SHIPS_AND_SIZES = (
    ("carrier", 5),
    ("battleship", 4),
    ("destroyer", 3),
    ("submarine", 3),
    ("patrol boat", 2),
)

ship_health = {
    "carrier"     : 5,
    "battleship"  : 4,
    "destroyer"   : 3,
    "submarine"   : 3,
    "patrol boat" : 2
}

# ... add your functions here
def constructing_playing_board():
    """
        This function will construct the 2d matrix that the game is played
        in.
    """
    playing_board = []

    for x in range(10):
        temp = []
        for y in range(10):
            temp.append("")
        playing_board.append(temp)

    return playing_board

def place_ship_in_playing_board(playing_board, ship, size, cords, direction):
    """
        This function will place the ships into the playingboard and return it.
    """
    if(direction == "horizontal"):
        for x in range(size):
            playing_board[cords[1]][cords[0]+x] = ship
    elif(direction == "vertical"):
        for x in range(size):
            playing_board[cords[1]+x][cords[0]] = ship

    return playing_board

def from_user_cords_to_program_cords(cords):
    """
        The user cords are pretty unusable for the computer so we turn it into
        a format we like. The y is constructed by getting the ascii value of the
        letter and - it with 65 to get the alphabetical order.
    """
    y = ord(cords[0])-65
    x = int(cords[1:]) - 1

    return [x, y]

def gather_fleet_positions():
    """
        This function will gather the fleets and place them on the board.
    """
    playing_board = constructing_playing_board()

    for ship, size in SHIPS_AND_SIZES:
        cords, direction = input(f"Location and orientation of your {ship}: ").split(" ")

        playing_board = place_ship_in_playing_board(playing_board, ship, size, from_user_cords_to_program_cords(cords), direction)
    
    return playing_board

def something_is_still_afloat(fleet):
    """
    This function checks if anything is afloat.
    """
    for x in fleet:
        for y in x:
            if(y):
                return True
    return False

def ask_where_to_attack():
    cords = from_user_cords_to_program_cords(input("Where to attack: "))

    return cords

def get_ship_at(cords, playing_board):
    return playing_board[cords[1]][cords[0]]
    
def report_hit(ship, cords, playing_board):
    if(ship_health[ship] == 1):
        print(f"You have sunk my {ship}")
    else:
        print(f"Hit, {ship}")
        ship_health[ship] -= 1
    
    playing_board[cords[1]][cords[0]] = ""

    return playing_board

def report_miss():
    print("Miss")

# You can use this game loop if you'd like
print("Specify the location of each ship in your fleet by providing the top/left coordinate and orientation.")
print("Examples: 'A2 vertical' or 'C3 horizontal'")

fleet = gather_fleet_positions()
while something_is_still_afloat(fleet):
    coordinates = ask_where_to_attack()
    ship = get_ship_at(coordinates, fleet)
    if ship:
        fleet = report_hit(ship, coordinates, fleet)
    else:
        report_miss()

print("The entire fleet has been sunk")