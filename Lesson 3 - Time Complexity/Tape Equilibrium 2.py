def minimum_difference_version2(A):
    """Returns the minimum of 
       |(A[0] + A[1] + ... + A[P-1]) - (A[P] + A[P+1] + ... + A[len(A)-1]) | 
       for P in [1, len(A)-1] """
    
    # Start with P == 1
    signed_difference = A[0] - sum(A[1:])
    differences = []
    differences.append(abs(signed_difference))
    
    # Traverse across A by taking A[P] from the right sum to the left
    # (left sum + A[P]) - (right sum - A[P]) = signed_difference + (2 * A[P])
    for P in range(1, len(A)-1):
        signed_difference += (2 * A[P])                      
        differences.append(abs(signed_difference))
        
    return min(differences)

 

    
   
