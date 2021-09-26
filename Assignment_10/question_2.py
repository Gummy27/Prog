BASE_PRICE = 1500


# Main program starts here
# It should mostly be a sequence of function calls
def main():
    list_of_toppings = user_input()
    print_out_pizza_info(list_of_toppings)

# Your functions should appear here

def user_input():
    """
    This is the user input part of the program. It will return a list
    of toppings that the user wants on their pizza.
    """
    toppings_tf = "y"
    list_of_toppings = []
    while(toppings_tf == "y"):
        toppings_tf = input("Would you like to add a topping(y/n)?: ")

        if(toppings_tf == "y"):
            topping_name = input("What topping would you like to add?: ")
            topping_price = input("What is the price of the topping?: ")

            list_of_toppings.append([topping_name, int(topping_price)])
    return list_of_toppings

def print_out_pizza_info(list_of_toppings):
    """
    This function will print all the information out and calculate the price.
    This function doesn't return anything.
    """
    print("Pizza with", end=" ")
    final_price = 0
    if(len(list_of_toppings) > 0):
        for index in range(len(list_of_toppings)):
            name, price = list_of_toppings[index]

            final_price += price
            if(index != len(list_of_toppings)-1):
                print(name, end=", ")
            else:
                print(name, end=" | ")
    else:
        print("no toppings", end=" | ")
    
    print(f"price: {final_price+BASE_PRICE}")

if __name__ == "__main__":
    main()