total_credits_int = 0 # Do not change this line
certificate_str = "" # Do not change this line

# Fill in the missing code below
num_years = int(input("How many years of university studies have you completed: ")) # Do not change this line

total_credits_int = 60 * num_years

if(total_credits_int >= 480):
    certificate_str = "a PhD"
elif(total_credits_int >= 300):
    certificate_str = "a MSc"
elif(total_credits_int >= 180):
    certificate_str = "a BSc"
else:
    certificate_str = "no degree yet, keep going!"

if num_years >= 0: # Do not change this line
    print("You have completed", total_credits_int ,"ECTS credits, and you have", certificate_str)  # Do not change this line
else:
    print("The number must be greater than or equal to zero.")