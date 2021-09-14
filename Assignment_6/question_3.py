items = input("Enter any items seperated by space: ")

# Complete the program below
for item in items.split(" "):
    repitition = int(input(f"Repeat {item} how many times?: "))

    print((item+" ")*repitition)