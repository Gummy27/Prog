RANK = 0
COUNTRY = 1
RATING = 2
BIRTHYEAR = 3

def main():
    filename = input("Enter filename: ")
    filestream = open_file(filename)
    if filestream:
        players_dict = create_players_dict(filestream)
        countries_dict = create_countries_dict(players_dict)
        birthyears_dict = create_birthyears_dict(players_dict)
        print_sorted(players_dict, countries_dict, "Players by country:")
        print()
        print_sorted(players_dict, birthyears_dict, "Players by birth year:")

def open_file(filename):
    try:
        with open(filename, "r") as filestream:
            return filestream.readlines()
    except FileNotFoundError:
        print("File was not found!")
        return None

def create_players_dict(filestream):
    players_dict = {}
    for line in filestream:
        rank, fullname, country, rating, birthyear = line.split(";")
        last_name, first_name = fullname.split(",")

        first_name = first_name.strip()
        last_name = last_name.strip()

        key = f"{first_name} {last_name}"

        players_dict[key] = (int(rank), country.strip(), int(rating), int(birthyear))

    return players_dict

def create_countries_dict(players_dict):
    country_dict = {}
    for player_name in players_dict:
        country = players_dict[player_name][COUNTRY]

        if country in country_dict:
            country_dict[country].append(player_name)
        else:
            country_dict[country] = [player_name]

    return country_dict

def create_birthyears_dict(players_dict):
    birthyears_dict = {}
    for player_name in players_dict:
        birthyear = players_dict[player_name][BIRTHYEAR]

        if birthyear in birthyears_dict:
            birthyears_dict[birthyear].append(player_name)
        else:
            birthyears_dict[birthyear] = [player_name]
    return birthyears_dict

def print_sorted(players_dict, sorted_dict, header):
    print_header(header)

    for country in sorted(sorted_dict):
        players_from_sorted = sorted_dict[country]
        average_rating_of_country = calculate_avg_rating(players_dict, players_from_sorted)

        print(f"{country} ({len(players_from_sorted)}) ({average_rating_of_country:.1f}):")

        for player_name in players_from_sorted:
            player_rating = players_dict[player_name][RATING]
            print("{:>40}{:>10d}".format(player_name, player_rating))

def calculate_avg_rating(players_dict, players_from_sorted):
    ratings = [players_dict[player][RATING] for player in players_from_sorted]
    return sum(ratings) / len(ratings)

def print_header(header):
    print(header)
    print("-"*len(header))

if(__name__ == "__main__"):
    main()