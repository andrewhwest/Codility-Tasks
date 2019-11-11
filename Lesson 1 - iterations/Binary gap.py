def solution(n):
    """returns the largest number zeros between two 1s in the binary representation of n"""
    
    n_binary = bin(n)[2:]     #[2:] removes '0b'   
    
    one_indexes = [index for (index, value) in enumerate(n_binary) if value == "1"]
    
    if len(one_indexes) == 1:    
        return 0                 
    #need at least two 1s for gaps 
    
    longest_gap = max((index - adjacent - 1) for index, adjacent in zip(one_indexes[1:], one_indexes))
    #works when n_binary has no zeros, eg "111"
    
    return longest_gap
    
print(solution(15))            #1111
print(solution(64))            #1000000
print(solution(1041))          #10000010001
print(solution(1147483647))    #1000100011001010011010111111111
m = 123456 ** 654321
print(len(bin(m)[2:]), solution(m))