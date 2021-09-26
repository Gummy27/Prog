def main():
    suffix = input("Enter a suffix for a country: ")
    suffix_counter = 0

    with open("countries.txt", "r") as file:
        for line in file.readlines():
            line_suffix = line[-(len(suffix)+1):].strip()

            if(line_suffix == suffix):
                print(line, end="")
                suffix_counter += 1
        print(f"{suffix_counter} countries with suffix '{suffix}'.")


if __name__ == "__main__":
    main()