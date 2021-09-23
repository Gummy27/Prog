def decimal_symbol_to_hex_symbol(dec_symbol):
    '''
        This function takes in a decimal symbol(number) and changes
        it into it's hex counterpart. Every number under 10 is unchanged
        but the others are changed using the ascii table.
    '''
    if(dec_symbol < 10):
        return str(dec_symbol)
    else:
        '''
            The hex symbols that represent 10 to 15 are the first 6 letters
            of the alphabet. The first capital letter of the alphabet is found
            at 65 in ascii. So we can easlily subtract 10 from the decimal number
            and then add 65 to it to get the desire letter.
        '''
        hex_ascii_pos = 65+(dec_symbol-10)
        return chr(hex_ascii_pos)

def decimal_to_hex_str(dec_int):
    '''
        This function takes in a decimal number and converts it
        into hex.
    '''

    hex_str = ""
    while(dec_int > 0):
        raw_hex_num = dec_int % 16
        hex_str += decimal_symbol_to_hex_symbol(raw_hex_num)

        dec_int = dec_int // 16
    
    return hex_str[::-1]

def hex_symbol_to_decimal_symbol(hex_symbol):
    '''
        This function takes in a hex symbol and changes it into it's
        decimal counterapart. Every number under 10 is unchanged
        but the others are changed using the ascii table.
    '''
    try:
        return int(hex_symbol)

    except:
        '''
            The hex symbols that represent 10 to 15 are the first 6 letters
            of the alphabet. So we can easily convert them into decimal by finding
            the position of the letter in the alphabet and then adding 10
            to it. So f.x. the ascii for A is 65 so all we have to do is 
            subtract 65 from it and then add 10 to find the decimal.
        '''
        dec_symbol = (ord(hex_symbol) - 65) + 10

        
        if(dec_symbol > 15):
            dec_symbol = None

        return dec_symbol

def hex_str_to_decimal(hex_str):
    '''
        This function takes in a hex number and converts it 
        into decimal
    '''

    dec_num = 0
    for index in range(len(hex_str)):
        # We loop backwards through the string so power reflects the number position.
        dec_symbol = hex_symbol_to_decimal_symbol(hex_str[::-1][index])

        if(dec_symbol != None):
            dec_num += dec_symbol*(16**index)
        else:
            dec_num = None
            break


    return dec_num

def display_menu():
    '''
        This function simply prints out the options for the user
    '''
    print()
    print("d. Decimal to hex")
    print("h. Hex to decimal")
    print("x. Exit")
    print()

def main():
    action = ""
    while(action != "x"):
        display_menu()
        action = input("Enter option: ")

        if(action == "d"):
            decimal_int = int(input("Decimal number: "))
            print("The hex is", decimal_to_hex_str(decimal_int))

        elif(action == "h"):
            hex_str = input("Hex number: ").upper()
            print("The decimal is", hex_str_to_decimal(hex_str))
            
        elif(action != "x"):
            print("Invalid option!")

# Main program starts here
if __name__ == "__main__":
    main()