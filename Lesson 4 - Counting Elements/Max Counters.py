class Counter_error(Exception):
    """Raised when a value in A isn't in [1,N+1]"""
    pass

def final_counter_values(N, A):
    """Returns the final value of the N counters
       after using counter operations determined by A"""
    
    #initialise counters
    counters = [0] * N
    
    for value in A:
        try:
            
            #increase(X) operation
            if 1 <= value <= N:
                counters[value-1] += 1
                
            #max counter operaton
            elif value == (N+1):
                counters = [max(counters)] * N
                
            #value not in [1,N+1]
            else:
                raise Counter_error
                
        except Counter_error:
            print("{0} is an invalid input for our counter operations".format(value))
            
    return counters
