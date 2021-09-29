def main():
    max_num = int(input("What should max_num be?: "))
    print(fizzbuzz_sum(max_num))

# fizzbuzz_sum definition goes here
def fizzbuzz_sum(max_num):
    fizzbuzz_list = []
    for x in range(1, max_num):
        if(x % 3 == 0 and x % 5 == 0):
            fizzbuzz_list.append(x)

    return sum(fizzbuzz_list)


# Main program starts here - DO NOT change it
if __name__ == "__main__":
    main()
