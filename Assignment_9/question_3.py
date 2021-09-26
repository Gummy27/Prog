def main():
    input_sequence = input("Enter in a sequence of numbers seperated by space: ")

    number_result = 0
    for number in input_sequence.split():
        try:
            # Check if number is a float point number
            if(number.count('.') == 0):
                number_result += int(number)
        except:
            pass
    print(number_result)


if __name__ == "__main__":
    main()