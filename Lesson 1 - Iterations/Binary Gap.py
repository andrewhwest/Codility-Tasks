def longest_binary_gap(N):
    """Returns the largest number of 0s between two 1s in the binary representation of n"""
    
    N_binary = bin(N)[2:]     #[2:] removes '0b'   
    
    one_indexes = [index for (index, value) in enumerate(N_binary) if value == "1"]
    
    if len(one_indexes) == 1:    
        return 0                 
    #need at least two 1s for gaps 
    
    longest_gap = max((index - adjacent - 1) for index, adjacent in zip(one_indexes[1:], one_indexes))
    #each gap is given by one_indexes[i] - one_indexes[i-1] - 1 
    #works when N_binary has no zeros, eg "1111"
    
    return longest_gap
    
