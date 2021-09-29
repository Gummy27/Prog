from math import sqrt

def main():
    a_list = get_list()
    print(prime_sum(a_list))

# These functions are given, do not change them, you can however call them.
def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def get_list():
    a_list = input("Enter elements of list seperated by commas: ").strip().split(",")
    a_list = [int(number) for number in a_list]
    return a_list

# implement prime_sum(a_list) here below
def prime_sum(list_of_numbers):
    return sum([number for number in list_of_numbers if is_prime(number)])

# main functionality
if __name__ == "__main__":
    main()