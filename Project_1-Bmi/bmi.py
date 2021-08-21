stones = float(input("Weight in stones: "))
pounds = float(input("Weight in pounds: "))
feet = float(input("Height in feet: "))
inches = float(input("Extra inches: "))

weight = stones * 6.3503 + pounds * 0.4540
height = feet * 30.48 + inches * 2.54

print("kg:", round(weight, 1))
print("cm:", round(height, 1))
print("BMI:", round(weight/((height/100)**2), 1))
