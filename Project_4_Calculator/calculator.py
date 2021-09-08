command = input("Enter an equation: ")

while(command != "q"):
    product = "e"
    first_num, operator, second_num = command.split(" ")

    try:
        # tölurnar eru kastaðar í float. Ef að gildið er ekki tala þá
        # kemur upp villa og forritið fer í except.
        first_num = int(first_num)
        second_num = int(second_num)

        # Hérna eru tölurnar lagðar saman og modúlaðar með 1 til að gá 
        # hvort þær séu með einhverja aukastafi.
        if((first_num + second_num) % 1 != 0 ):
            print("Invalid operands")
        elif(operator == "+"):
            product = round(first_num + second_num, 2)
        elif(operator == "-"):
            product = round(first_num - second_num, 2)
        elif(operator == "/"):
            if(second_num != 0):
                product = round(first_num / second_num, 2)
            else:
                print("Can't divide by 0")
        elif(operator == "*"):
            product = round(first_num * second_num, 2)
        else:
            print("Invalid operator")
        
        # Gáð er hvort það sé eitthvað í product svo að það prentist ekki 
        # út ef að það er invalid operator
        if(product != "e"):
            # Þetta einfaldlega formattar töluna þannig að hún hafi alltaf 2 aukastafi.
            print(f"Result: {product:.2f}")

    except:
        print("Invalid operands")
    

    command = input("Enter an equation: ")