# You might need this to calculate a square root using math.sqrt
import math

# Loop until the user types in -1
num_input = int(input("Enter a number (-1 to exit) "))
counter = 0

prev_average = 0
prev_cumulative = 0

while(num_input >= 0):
    counter += 1
    # Calculate the cumulative moving average and standard deviation
    current_average = prev_average + (num_input - prev_average)/counter
    prev_average = current_average

    current_cumulative = prev_cumulative + ((counter-1)/counter)*((counter - prev_average)**2)
    prev_cumulative = current_cumulative

    if(counter - 1 > 0):
        standard_deviation = current_cumulative/(counter)
    else:
        standard_deviation = 0

    # Print them out within the loop
    print("Average:", round(current_average, 2))
    print("Standard deviation:", round(standard_deviation, 2))
    num_input = int(input("Enter a number (-1 to exit) "))

