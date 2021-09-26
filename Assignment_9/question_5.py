def main():
    name = get_name()
    age = get_age()

    print(f"Hello {name}, age {age}.")

def get_name():
    """
    This function takes in input from user and checks if name is valid.
    """
    valid_name = False
    while(not valid_name):
        name = input("Enter your name: ")

        valid_name = True
        if(name):
            for letter in name:
                try:
                    int(letter)
                    valid_name = False
                    break

                except:
                    pass
        else:
            valid_name = False
    
        if(not valid_name):
            print("Please enter a valid name.")
    return name
        
            

def get_age():
    """
    This function takes in age of user and checks if it's valid.
    """
    valid_age = False
    while(not valid_age):
        try:
            age = int(input("Enter your age: "))

            if(0 <= age <= 125):
                valid_age = True
            else:
                print("Age is not in range!")
        
        except:
            print("Please enter an integer.")
    return age

if __name__ == "__main__":
    main()