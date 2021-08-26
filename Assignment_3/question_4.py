n = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below

counter = 0
result = 0
while(counter < len(str(n))):
    result += int(str(n)[counter])
    counter += 1

print(result)