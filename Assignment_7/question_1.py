# alphabetically_first definition goes here
def alphabetically_first(word1, word2):
    '''
    This function finds which word is first alphabetically.
    '''
    if(ord(word1[0]) > ord(word2[0])):
        return word2
    else:
        return word1