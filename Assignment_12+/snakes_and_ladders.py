import random

# ... add your functions here

def read_board_layout_from_input():
    number_of_snakes_and_ladders = int(input("Number of snakes and ladders: "))

    snakes, ladders = [], []
    for x in range(number_of_snakes_and_ladders):
        beginning, end = input(f"Snake/ladder {x+1} leads from where to where: ").split(" ")

        if(int(beginning) < int(end)):
            ladders.append([int(beginning)-1, int(end)-1])
        else:
            snakes.append([int(beginning)-1, int(end)-1])
    return snakes, ladders

def read_player_names_from_input():
    player1 = input("Name of player 1: ")
    player2 = input("Name of player 2: ")

    return player1, player2

def play_game(snakes, ladders, player1, player2):
    player_pos = [0, 0]
    player_names = [player1, player2]
    playing = False
    roll = 0
    while(player_pos[0] < 100 and player_pos[1] < 100):
        if(roll != 6):
            playing = not playing

        roll = roll_die()
        player_pos[playing] += roll
        print(f"{player_names[playing]} rolled {roll} and is now at square {player_pos[playing]}")
        
        snake_ladder, new_pos = check_snakes_and_ladders(snakes, ladders, player_pos[playing])

        if(snake_ladder == "s"):
            print(f"Darn! A bloody snake brought {player_names[playing]} down to square {new_pos+1}")
            player_pos[playing] = new_pos
        elif(snake_ladder == "l"):
            print(f"Splendid! {player_names[playing]} climbed a ladder up to square {new_pos+1}")
            player_pos[playing] = new_pos


    return player_names[playing]

def check_snakes_and_ladders(snakes, ladders, pos):
    for x in snakes:
        if(x[0] == pos):
            return "s", x[1]
    
    for x in ladders:
        if(x[0] == pos):
            return "l", x[1]
    
    return "", 0

def declare_winner(winner):
    print(f"{winner} won the game")


# DON'T CHANGE THE CODE BELOW
def main():
    # Ensure that games play out deterministically by specifying the random seed.
    # This is needed to ensure that the sequence of die rolls is exactly as expected by the tests in Mimir.
    random.seed(1337)
    snakes, ladders = read_board_layout_from_input()
    player1, player2 = read_player_names_from_input()
    winner = play_game(snakes, ladders, player1, player2)
    declare_winner(winner)


# Make use of this method whenever a player rolls a die
def roll_die() -> int:
    """ Simulate a roll of a 6-sided die """
    return random.randint(1, 6)


main()
