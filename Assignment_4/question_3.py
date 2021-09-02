size = int(input("How large is the square?: "))

# Write your solution here below
for x in range(size):
    for i in range(size):
        if(i == 0 or i == size-1 or x == 0 or x == size-1):
            print("* ", end="")
        else:
            print("  ", end="")
    print()