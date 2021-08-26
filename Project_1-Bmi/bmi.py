stones = float(input("Weight in stones: "))
pounds = float(input("Extra pounds: "))
feet =   float(input("Height in feet: "))
inches = float(input("Extra inches: "))

weight_kg = stones * 6.3503 + pounds * 0.4540
height_cm = feet * 30.48 + inches * 2.54
# bmi = kg/m**2
bmi = weight_kg/((height_cm/100)**2)

print()
print("kg:",  round(weight_kg, 1))
print("cm:",  round(height_cm, 1))
print("BMI:", round(bmi, 1))
