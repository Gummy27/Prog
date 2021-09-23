# extract_first_number_from_string definition goes here
def extract_first_number_from_string(number_string):
    '''
    Finds the first number in a string
    '''
    for word in number_string.split(" "):
        try:
            return(int(word))
        except:
            pass
    return -1