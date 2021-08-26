num_int = int(input("Enter a number greater than or equal to 2: ")) # Do not change this line
counter = 2

# Fill in the missing code below
if(num_int < 2):
    print("The number is too small.")
else:
    while(counter <= num_int):
        print(counter)
        counter += 2