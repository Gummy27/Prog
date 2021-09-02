# Don't change the following lines
import math

number_of_cycles = float(input("Number of cycles: "))
number_of_lines = int(input("Stretched over how many lines? "))

radians_per_line = number_of_cycles * 2 * math.pi / number_of_lines

for line_number in range(number_of_lines):
    radians = line_number * radians_per_line 
    print("X"*round((math.sin(radians)+1)*20))

# ...now fill in the rest