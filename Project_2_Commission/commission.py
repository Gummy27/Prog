# Paper reams = 10$
# Printers = 150$


total_sales = 0
total_commission = 0
print("Welcome to Dunder Mifflin!")
while(True):
    yes_no = input("Would you like to add a sale (y/n)?: ")
    if(yes_no == "y"):
        product = input("paper or printer: ")
        if(product == "paper"):
            units = int(input("# of paper piles: "))
            total_sales += 1
            total_commission += (10*units)*0.15

        elif(product == "printer"):
            units = int(input("# of printers: "))
            total_sales += 1
            total_commission += (150*units)*0.3
            
        else:
            print("You did neither type in paper nor printer")
        print(f"You've made {round(total_commission)} today with {total_sales} sales")
    elif(yes_no == "n"):
        break
    else:
        print("Please try agaub")