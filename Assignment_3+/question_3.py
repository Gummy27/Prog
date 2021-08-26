from random import randint
from math import floor

# These lines you can keep as is
print("Think of a number between 1 and 100 (inclusive)")
print("I am going to guess what it is")
input("Press enter when you are ready to play")

# Here you might want to initialize some variables
cmd = ""
guess = 50
guess_roof = 100
guess_floor = 0
counter = 1
cheating = True
# Then start a while loop
while(cmd != "c" and cmd != "q" and counter <= 7):
    # These lines you can keep as is
    print("Is the number", guess, "?")
    print("Type one of the following letters and press enter:")
    print("h: if the guess is too (h)igh")
    print("l: if the guess is too (l)ow")
    print("c: if the guess is (c)orrect")
    print("q: to (q)uit the game")
    cmd = input()
    if(cmd == "l"):
        guess_floor = guess
        guess = guess_roof - floor((guess_roof - guess) // 2) 
    elif(cmd == "h"):
        guess_roof = guess-1
        guess = guess_floor + floor((guess - guess_floor) // 2)
    elif(cmd == "c"):
        print("I AM VICTORIOUS")
        cheating = False
    elif(cmd == "q"):
        print("Quitter")
        cheating = False
    counter += 1
    
    # Now it's up to you to check the command and take appropriate action


# If you detect that the user has not been truthful, you should print the following
if(counter >= 7 and cheating):
    print("Tsk, tsk, don't try to cheat me")
