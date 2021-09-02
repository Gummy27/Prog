n = int(input("Enter how many numbers you want to input(>0): ")) # Do not change this line

# Fill in the missing code
for x in range(n):
    number = int(input("Enter an integer: "))
    if(x == 0):
        max_num = number
        min_num = number
        continue

    if(max_num < number):
        max_num = number
    elif(min_num > number):
        min_num = number

print("Highest number from input:", max_num)
print("Lowest number from input:", min_num)