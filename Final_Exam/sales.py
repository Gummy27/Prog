def main():
    file_name = input("Enter file name: ")
    file_object = open_file(file_name)
    # Your continue the program from here
    if file_object:
        file_dict = process_file_into_dict(file_object)

        want_total = input("Show totals per store (y/n)?: ")

        print_out_file_dict(file_dict, want_total)
    else:
        print(f"File {file_name} not found")

def open_file(filename):
  '''Opens the given file, returning its file object if found, otherwise None'''
  try:
    file_object = open(filename, 'r')
    return file_object
  except FileNotFoundError:
    return None

def process_file_into_dict(file_stream: object) -> dict:
    """
        This function will take in a file stream and turn it into a 
        dictionary of information.
    """
    split_lines = file_stream.read().split("\n")

    new_dict = {}
    for line in split_lines:
        split_line = line.split(";")

        key = split_line[0]
        prices = list(map(float, split_line[1:]))

        if key not in new_dict:
            new_dict[key] = prices
        else:
            for index in range(len(prices)):
                new_dict[key][index] += prices[index]

    file_stream.close()
    return new_dict

def print_out_file_dict(file_dict: dict, total: str) -> None:
    """
        This function will print out the file dict in an
        organized manner.
    """
    file_dict = calculate_icecream_total(file_dict)

    for icecream in sorted(file_dict):
        if icecream:
            print(construct_line_in_columns(icecream, file_dict[icecream]))

    if total == "y":
        store_total = calculate_store_total(file_dict)
        print(construct_line_in_columns("Total:", store_total))

def calculate_store_total(file_dict: dict) -> list:
    """
        This function will calculate the total for each store and
        return it as a list.
    """
    store_total = []
    for icecream in file_dict:
        for index in range(len(file_dict[icecream])):
            try:
                store_total[index] += float(file_dict[icecream][index])
            except IndexError:
                store_total.append(float(file_dict[icecream][index]))
    return store_total[:-1]

def calculate_icecream_total(file_dict: dict) -> dict:
    """
        This function calculates the total sales of each icecream.
        This information will be appended to file dict and file dict
        will be returned.
    """
    for icecream in file_dict:
        if icecream != "Total:":
            total = sum(file_dict[icecream])
            file_dict[icecream].append(total)
    return file_dict

def construct_line_in_columns(name: str, prices: list) -> str:
    """
        This function will print out the information spaced out.
    """
    return_string = name + " " * (15 - len(name))

    for price in prices:
        price_string = f"{float(price):.2f}"
        return_string += " "*(12-len(price_string)) + price_string
    
    return return_string

# Main program starts here.  Do NOT change the starter code.
if __name__ == "__main__":
    main()