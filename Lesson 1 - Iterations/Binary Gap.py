def one_indices(binary_number):
    """Returns a list of the indices where there are 1s in a binary number"""
    
    return [index for (index, value) in enumerate(binary_number) if value == "1"]

def longest_binary_gap(N):
    """Returns the largest number of 0s closed inbetween two 1s in the binary representation of N"""
    
    N_binary = bin(N).split('b')[1]  
    
    # Need at least two 1s for gaps
    if len(one_indices(N_binary)) == 1:    
        return 0                 
    else: 
        longest_gap = max( (index - adjacent - 1) for index, adjacent 
                                                  in zip(one_indices(N_binary)[1:], 
                                                         one_indices(N_binary))
                         ) 
        return longest_gap