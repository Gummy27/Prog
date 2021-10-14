def user_input():
    """
        This function takes in user input and returns it.
    """
    try:
        number_of_shares = int(input("Enter number of shares: "))

        dollars, numerator, denominator = input("Enter price (dollars, numerator, denominator): ").split(" ")

        return number_of_shares, dollars, numerator, denominator

    except ValueError:
        print("Invalid number of shares!")
        
        return None, None, None, None


def convert_to_stock_price(dollars, numerator, denominator):
    """
        This function takes in the user stock price input and converts it into a float number
    """
    return float(dollars) + (float(numerator)/float(denominator))

def print_out_stock_price(number_of_shares, dollars, numerator, denominator, price):
    """
        This function prints out all the information.
    """
    print(f"{number_of_shares} shares with market price {dollars} {numerator}/{denominator} have value ${number_of_shares*price:.2f}")

def main():
    continue_program = "y"
    while(continue_program == "y"):
        number_of_shares, dollars, numerator, denominator = user_input()

        if(number_of_shares == None):
            continue

        price = convert_to_stock_price(dollars, numerator, denominator)

        print_out_stock_price(number_of_shares, dollars, numerator, denominator, price)

        continue_program = input("Continue (y/n): ")


main()