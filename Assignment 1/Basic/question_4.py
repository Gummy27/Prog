import math

val_a_str = input("Enter the value for a: ") # Do not change this line
val_b_str = input("Enter the value for b: ") # Do not change this line
val_c_str = input("Enter the value for c: ") # Do not change this line
# Fill in the missing code below

s = (int(val_a_str) + int(val_b_str) + int(val_c_str)) / 2

area = math.sqrt(s*(s-int(val_a_str))*(s-int(val_b_str))*(s-int(val_c_str)))

print("The area of the triangle is", area) # Do not change this line