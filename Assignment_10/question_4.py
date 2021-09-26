MAX = 1000000

def main():
    for i in range(10, MAX + 1):
        if has_property(i):
            print(i)

# Write your functions here below

def has_property(x):
    for y in range(1, len(str(x))):
        new_x = str(x*(y+1))

        if(sorted(new_x) != sorted(str(x))):
            return False
    return True


if __name__ == "__main__":
    main()