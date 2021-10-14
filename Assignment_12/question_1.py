def remove_odds(number_list):
    for x in range(len(number_list), 0, -1):
        if(number_list[x-1] % 2 != 0):
            number_list.pop(x-1)
    return number_list

def extract_evens(number_list):
    evens_list = []
    for x in number_list:
        if(x % 2 == 0):
            evens_list.append(x)
    return evens_list

def main():
    # Main starts here
    a_list = [1,1,2,3,4,5]
    print(a_list)
    remove_odds(a_list)
    print(a_list)
        
    b_list = [1,1,2,3,4,5,6,7,8,9,10]
    c_list = extract_evens(b_list)
    print(b_list)
    print(c_list)

if __name__ == "__main__":
    main()