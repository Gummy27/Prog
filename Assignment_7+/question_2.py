def remove_at(sequence, index_to_remove):
    """ Removes an element from a sequence at the specified index. 
    
    Returns the updated sequence and the element that was removed, in that order.
    """
    # ... and the rest is up to you

    removed_element = sequence[index_to_remove]
    new_sequence = sequence[:index_to_remove] + sequence[index_to_remove+1:]

    return new_sequence, removed_element 
