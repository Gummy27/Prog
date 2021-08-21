d = float(input("What is the diameter?"))

import math

radius = d / 2

volume = (4/3)*math.pi*(radius**3)

volume_of_half_sphere = volume / 2

print("The volume of the half-sphere is", volume_of_half_sphere)