num_int = int(input("Input a number: "))    # Do not change this line

# Fill in the missing code

'''
The algorithm will first initialize a variable as 0 to keep track
of the highest number. In each iteration of the while loop it will
check if the new number is larger than the old one. If that is true
then the new number is stored in the max_int variable.
'''

max_int = 0
while(num_int > 0):
    if(max_int < num_int):
        max_int = num_int
    num_int = int(input("Input a number: "))


print("The maximum is", max_int)    # Do not change this line
