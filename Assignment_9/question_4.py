def main():
    file_name = input("Enter the filename: ")

    with open(file_name, "r") as file:
        for line in file.readlines():
            for word in line.split(" "):
                print(word[::-1], end=" ")

if __name__ == "__main__":
    main()