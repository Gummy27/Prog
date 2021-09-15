def find_index_of_nth_occurrence(sequence, element_to_find, occurrence):
    """ Returns the location of the n-th occurrence of an element within a sequence """
    # ... and the rest is up to you

    for index in range(len(sequence)):
        if(sequence[index] == element_to_find):
            occurrence -= 1

            if(occurrence == 0):
                return index
    return -1
        