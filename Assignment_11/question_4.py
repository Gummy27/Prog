# Main program starts here - DO NOT change it
def main():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    a_tuple = list_to_bool_tuple(a_list)
    print(a_tuple)
    
#list_to_bool_tuple function goes here
def list_to_bool_tuple(string_list):
    temp = []
    for x in string_list:
        """
            "0" is true in bool but we want the program to interpret it as the integer
            0 so we try to cast it into int. 
        """
        try:
            temp.append(bool(int(x)))
        except:
            temp.append(bool(x))
    return tuple(temp)


if __name__ == "__main__":
    main()