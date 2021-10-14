GENERIC_PROMPT = "Enter elements of {}, seperated by commas: "


def main():
    int_list = get_list(GENERIC_PROMPT.format("int_list"))
    exponent_list = get_list(GENERIC_PROMPT.format("exponent_list"))
    if int_list and exponent_list:
        x = int(input("x: "))

        result = check_powers(int_list, exponent_list, x)
        print(result)
    else:
        print("Error: enter only integers.")


def get_list(prompt):
    a_list = input(prompt).split(",")
    try:
        a_list = [int(elements) for elements in a_list]
        return a_list
    except ValueError:
        return None


# Implement the function "check_powers" here
def check_powers(int_list, exponant_list, x=2):
    for k in exponant_list:
        if(x**k in int_list):
            return True
    return False



if __name__ == "__main__":
    main()
