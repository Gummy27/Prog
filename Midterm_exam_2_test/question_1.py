CHOICE_SUM = 1
CHOICE_PRODUCT = 2
CHOICE_EXIT = 9

def user_input():
    """
        This function will print out choice menu and take in the user input.
    """
    print(f"{CHOICE_SUM}: Compute the sum of 1..n")
    print(f"{CHOICE_PRODUCT}: Compute the product of 1..n")
    print(f"{CHOICE_EXIT}: Quit")

    try:
        choice = int(input("Choice: "))
        n = ""

        if(choice != 9):
            if(choice in [CHOICE_SUM, CHOICE_PRODUCT, CHOICE_EXIT]):
                n = int(input("Enter value for n: "))

        return choice, n

    except ValueError:
        return None, None

def sum_of_series(n):
    """
        This function will calculate the sum of series 1 to n.
    """
    result = 0
    for x in range(n):
        result += (x+1)
    return result

def product_of_series(n):
    """
        This function will calculate the product of series 1 to n.
    """
    result = 1
    for x in range(n):
        result *= (x+1)
    return result

def main():
    choice = 0
    while(choice != 9):
        choice, n = user_input()

        if(choice == CHOICE_SUM):
            print(f"The result is: {sum_of_series(n)}")
        elif(choice == CHOICE_PRODUCT):
            print(f"The result is: {product_of_series(n)}")

main()