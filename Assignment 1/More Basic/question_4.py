import math
length_cm = 50
degrees_str = input("Roof's angle in degrees: ")
# Convert input to integer
degrees_int = int(degrees_str)

# Convert degrees to radians in order to use the trigonometric functions in the math module
radians_int = math.radians(degrees_int)

# Calculate the the height of the triangle
height_cm = length_cm*math.tan(radians_int)
print("To make the platform level, the height must be", round(height_cm, 1), "cm")