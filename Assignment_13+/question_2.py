def shuffle(original_list: list, start_from_back: bool=False) -> list:
    """
        This function takes a list and a bool value as parameters.
        It will take this list and shuffle it into a new list and then return it. 
        The bool value specifies how you want the list to be shuffled.
    """
    n = len(original_list)
    counter = 0

    new_list = []
    for x in range(n):
        """
            This series that we follow the odd even number sequence. So I used that 
            sequence to generate the new list. The user can decide that he wants the
            shuffle to start from the back. This series also follow the odd even 
            sequence except it starts at an odd number. So we plus the x value by
            1 to shift it. 
        """
        if((x+start_from_back) % 2 == 0):
            index = counter
            counter += 1
        else:
            index = n-(counter+start_from_back)
        new_list.append(original_list[index])

    return new_list

print(shuffle([1, 2, 3, 4, 5, 6], True))