num_input = int(input("Input an integer (0 to quit): "))

counter = 0

sum_of_even = 0
sum_of_odd = 0

even_counter = 0
odd_counter = 0

while(num_input):
    if(num_input < 0):
        print("Ignoring this negative number!")
    elif(num_input % 2 == 0):
        sum_of_even += num_input
        even_counter += 1
    else:
        sum_of_odd += num_input
        odd_counter += 1
    num_input = int(input("Input an integer (0 to quit): "))

print("Sum of even: ", sum_of_even) 
print("Sum of odd: ", sum_of_odd)
print("Even count: ", even_counter)
print("Odd count: ", odd_counter)
