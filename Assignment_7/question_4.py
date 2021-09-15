# sum_of_range definition goes here
def sum_of_range(start, end, step):
    '''
    Sums up range with specific parameters.
    '''
    range_sum = sum(range(start, end+1, step))
    
    return range_sum