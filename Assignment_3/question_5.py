k = int(input("Enter value for k: ")) # Do not change this line

# Fill in the missingcode below

l = int(input("Enter a value: "))
x = 0
while(x + l <= k):
    x += l
    l = int(input("Enter a value: "))

print("Sum:", x)