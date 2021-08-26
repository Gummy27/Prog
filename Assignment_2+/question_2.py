p1_move = input("Player 1's move: ")
p2_move = input("Player 2's move: ")

# ...now fill in the rest
if(p1_move == p2_move):
    print("It's a draw")
else:
    if(p1_move == "rock"):
        if(p2_move == "paper"):
            print("Winner: Player 2")
        else:
            print("Winner: Player 1")
    elif(p1_move == "scissors"):
        if(p2_move == "rock"):
            print("Winner: Player 2")
        else:
            print("Winner: Player 1")
    elif(p1_move == "paper"):
        if(p2_move == "scissors"):
            print("Winner: Player 2")
        else:
            print("Winner: Player 1")