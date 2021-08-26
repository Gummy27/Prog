n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
if(n != 1):
    prime = True
    counter = 2
    while(counter < n):
        if(n % counter == 0):
            prime = False
            break
        counter += 1
else:
    prime = False

# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")