val_a_int = int(input("Enter the value for a: ")) # Do not change this line
val_b_int = int(input("Enter the value for b: ")) # Do not change this line
val_c_int = int(input("Enter the value for c: ")) # Do not change this line
 
# Fill in the missing code below


discriminant = val_b_int**2-(4*val_a_int*val_c_int)

if(discriminant > 0):
    print("2 solutions.")
elif(discriminant == 0):
    print("1 solution.")
else:
    print("No solutions.")