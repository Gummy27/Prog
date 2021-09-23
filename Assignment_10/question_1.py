def main():
    add_to_list = ""
    result_list = []
    chain_list = []
    chain = ""
    while(add_to_list != "x"):
        add_to_list = input("Enter a word to be added to the list: ")

        if(add_to_list != "x"):
            if(chain == add_to_list[0] or chain == ""):
                chain = add_to_list[-1]
                chain_list.append(add_to_list)
            result_list.append(add_to_list)
    
    print(result_list)

    for item in chain_list:
        print(item)



if __name__ == "__main__":
    main()
