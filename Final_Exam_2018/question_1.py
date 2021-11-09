def main():
    file_data = open_file("flights.txt")

    flights_dict = file_data_into_dict(file_data)

    print_out_dict(flights_dict)

def open_file(filename: str) -> str:
    """
        This function opens the file and returns the lines of 
        the file.
    """
    with open(filename, 'r') as file:
        return file.readlines()

def file_data_into_dict(file_data: str) -> dict:
    """
        This function takes in file data and returns it split into dict
    """
    temp_dict = {}
    
    for line in file_data:
        line = line.strip()

        name, country = line.split(" ")
 
        if name not in temp_dict:
            temp_dict[name] = set()
        temp_dict[name].add(country)
        
    return temp_dict

def print_out_dict(flights_dict: dict) -> None:
    """
        This function prints out the dict.
    """
    for name in sorted(flights_dict):
        print(f"{name}:")

        for country in sorted(flights_dict[name]):
            print(f"\t{country}")
    
    name, record = find_most_traveled(flights_dict)
    print(f"{name} has been to {record} countries")

def find_most_traveled(flights_dict: dict) -> list: 
    """
        This function finds the most traveled person in the flight
    """
    record = 0
    for name in flights_dict:
        if len(flights_dict[name]) > record:
            record = len(flights_dict[name])
            name_of_traveler = name
    return name_of_traveler, record

if __name__ == "__main__":
    main()