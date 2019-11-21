def final_counter_values(N, A):
    """Returns the final value of the N counters
       after using counter operations determined by A"""
    
    counters = [0] * N
    
    for value in A:
        #try:
            if 1 <= value <= N:
                counters[value-1] += 1
            elif value == (N+1):
                counters = [max(counters)] * N
        #except value not in range(1,N+1):
           # print("{0} is an invalid input for our counter operations".format(value))
            
    return counters
