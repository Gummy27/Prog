email_address = input("Email address: ")
print("Checking...")

# ...and the rest is up to you
last_symbol = ""
is_legit = True
number_of_at = 0
number_of_dots = 0

for index in range(len(email_address)):
    if(email_address[index] == "@"):
        number_of_at += 1
        number_of_dots = 0
        if(last_symbol == ""):
            print(" "+email_address)
            print("^--this bit is missing")
            is_legit = False
            break

        elif(index == len(email_address)-1):
            print(email_address)
            print((" "*(index+1)) + "^--this bit is missing")
            is_legit = False
            break

        elif(number_of_at > 1):
            print(email_address)
            print((" "*index) + "^--there's an extra @ symbol here")
            is_legit = False
            break

        elif(last_symbol == "."):
            print(email_address)
            print((" "*(index-1)) + "^--there's a dot here that probably shouldn't")
            is_legit = False
            break

    elif(email_address[index] == "."):
        number_of_dots += 1
        if(last_symbol == ""):
            print(email_address)
            print("^--there's a dot here that probably shouldn't")
            is_legit = False
            break

        elif(last_symbol == "."):
            print(email_address)
            print((" " * (index-1)), "^--there are consecutive dots here")
            is_legit = False
            break

        elif(index == len(email_address)-1):
            print(email_address)
            print((" " * (index-2)), "^--there's a dot here that probably shouldn't")
            is_legit = False
            break
        
    last_symbol = email_address[index]

if(is_legit):
    if(number_of_dots == 0):
        print("The top-level-domain is missing. Did you perhaps intend to write " + email_address + ".com?")
    elif(number_of_at == 0):
        print("@ symbol is missing")
    else:
        print("Seems legit")
