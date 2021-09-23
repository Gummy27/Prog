# is_substring definition goes here
def is_substring(sub_string, main_string):
    '''
    This function checks if a string is a substring of other string.
    '''

    for index in range(len(main_string) - len(sub_string)):
        if(main_string[index:index+len(sub_string)] == sub_string):
            return True
    return False