def minimum_difference(A):
    """Returns the minimum difference when splitting A into two parts"""
    
    #start with P == 1
    signed_difference = A[0] - sum(A[1:])
    differences = []
    differences.append(abs(signed_difference))
    
    #traverse across A by taking A[P] from the right sum to the left
    #(left sum + A[P]) - (right sum - A[P]) = signed_difference + (2 * A[P])
    for P in range(1, len(A)-1):
        signed_difference += (2 * A[P])                      
        differences.append(abs(signed_difference))
        
    return min(differences)

 

    
   