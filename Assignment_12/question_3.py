def main():
    a_list = [3, 9, 5, 1, 6, 8]
    print(f"{a_list}")
    remove_min_and_max(a_list)
    print(f"{a_list}")

    b_list = [9, 2, 3, 6, 1, 8, 7]
    c_list = remove_min_and_max_2(b_list)
    print(f"{b_list}")
    print(f"{c_list}")


def find_min_and_max_index(a_list):
    min_index = 0
    max_index = 0
    for i in range(1, len(a_list)):
        if a_list[min_index] > a_list[i]:
            min_index = i
        if a_list[max_index] < a_list[i]:
            max_index = i
    return min_index, max_index
    
def remove_min_and_max(a_list):
    min_index, max_index = find_min_and_max_index(a_list)

    a_list.pop(max([min_index, max_index]))
    a_list.pop(min([min_index, max_index]))
    
    
def remove_min_and_max_2(a_list):
    min_index, max_index = find_min_and_max_index(a_list)

    new_list = []
    for x in range(len(a_list)):
        if(x != min_index and x != max_index):
            new_list.append(a_list[x])
    return new_list

if __name__ == "__main__":
    main()