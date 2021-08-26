num_int = int(input("Enter a number: ")) # Do not change this line

# Fill in the missing code below
if(num_int <= 0):
    print("The number is too small.")
else:
    if(num_int % 2 == 0):
        counter = 2
    else:
        counter = 1
    while(counter <= num_int):
        print(counter)
        counter += 2