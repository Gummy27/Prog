r_0_str = input("What's the basic reproduction rate (R_0)? ")
# Convert input to float
r_0_int = float(r_0_str)

# Calculate the expected number of cases after 3 rounds of transmission originating
# from kitten Zero

total_cases = r_0_int**0+r_0_int**1+r_0_int**2+r_0_int**3
print("Total cases after 3 rounds of transmission:", round(total_cases))