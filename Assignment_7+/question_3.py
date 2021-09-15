def insert_at(sequence, index, element):
    """ Inserts an element at the specified location in a sequence and returns the updated sequence. """
    # ... and the rest is up to you

    new_sequence = sequence[:index] + element + sequence[index:]
    return new_sequence