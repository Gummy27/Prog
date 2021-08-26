import math

n = int(input("Enter a number: ")) # Do not change this line
print("Primes in the range", n*n, "and", (n+1)*(n+1), "are:") # Do not change this line

i = n*n
while i < ((n+1)*(n+1)):
    is_prime = True
    # Fill in the missing code below

    counter = 2
    while(counter < i):
        if(i % counter == 0):
            is_prime = False
            break
        counter += 1



    # We recommond you keep the following code unchanged
    if is_prime:
        print(i) # We recommend you not change this line
    i += 1