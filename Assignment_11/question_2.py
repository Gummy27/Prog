# Main program starts here
def main():
    home_addresses = get_home_addresses()
    print(home_addresses)
    street_and_number = get_tuple_from_home_addresses(home_addresses)
    print(street_and_number)

# Write your functions here
def get_home_addresses():
    user_input = ""
    addresses_list = []
    while(user_input != "q"):
        user_input = input("Home address: ")
        if(user_input != "q"):
            addresses_list.append(user_input)

    return addresses_list

def get_tuple_from_home_addresses(home_addresses):
    home_addresses_tuple = []
    for address in home_addresses:
        street_name, number = address.split(" ")
        home_addresses_tuple.append((street_name, number))
    
    return home_addresses_tuple



if __name__ == "__main__":
    main()