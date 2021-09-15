def find_index_of_nth_occurrence(sequence, element_to_find, occurrence):
    """ Returns the location of the n-th occurrence of an element within a sequence """
    # ... and the rest is up to you

    for index in range(len(sequence)):
        if(sequence[index] == element_to_find):
            occurrence -= 1

            if(occurrence == 0):
                return index
    return -1

def remove_at(sequence, index_to_remove):
    """ Removes an element from a sequence at the specified index. 
    
    Returns the updated sequence and the element that was removed, in that order.
    """
    # ... and the rest is up to you

    removed_element = sequence[index_to_remove]
    new_sequence = sequence[:index_to_remove] + sequence[index_to_remove+1:]

    return new_sequence, removed_element 

def insert_at(sequence, index, element):
    """ Inserts an element at the specified location in a sequence and returns the updated sequence. """
    # ... and the rest is up to you

    new_sequence = sequence[:index] + element + sequence[index:]
    return new_sequence


def move_one(from_pillar, to_pillar, state):
    """ Moves the topmost disc from one pillar to another and returns the updated state representation. """
    # ... implement this method, utilizing the functions defined above

    disc_to_be_moved_index = find_index_of_nth_occurrence(state, "|", from_pillar) - 1
    new_disc_index = find_index_of_nth_occurrence(state, "|", to_pillar)
    print(disc_to_be_moved_index, new_disc_index)
    
    
    state = insert_at(state, new_disc_index, state[disc_to_be_moved_index])

    '''
    When the new disc is inserted backwards into the state it the index skews by 1.
    To avoid removing the wrong index this if statement is implemented.
    '''
    if(from_pillar > to_pillar):
        state, _ = remove_at(state, disc_to_be_moved_index+1)
    else:
        state, _ = remove_at(state, disc_to_be_moved_index)

    return state
print(move_one(1, 3, "321|||"))