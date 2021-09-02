initial_amount = float(input("Enter the initial amount: ")) # Do not change this line
interest = float(input("Enter the interest(%): ")) # Do not change this line
years = int(input("Enter for how many years: ")) # Do not change this line

interest = interest / 100

current_amount = initial_amount
for x in range(years):
    current_amount = current_amount  + current_amount * interest


print(f"Amount after {years} years: {round(current_amount, 2)}")