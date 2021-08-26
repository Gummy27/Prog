birth_year = int(input("What year were you born?: ")) # Do not change this line

# Finish the program here below 
if(1946 <= birth_year <= 1964):
    print("You are a baby boomer.")
elif(1965 <= birth_year <= 1980):
    print("You are part of generation X.")
elif(1981 <= birth_year <= 1996):
    print("You are a millenial.")
elif(1997 <= birth_year <= 2012):
    print("You are part of generation Z.")
elif(birth_year > 2012):
    print("You are part of generation A.")
else:
    print("You are unlabeled.")