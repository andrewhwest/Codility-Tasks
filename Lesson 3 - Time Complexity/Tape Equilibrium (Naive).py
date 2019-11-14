def minimum_difference(A):
      """Returns the minimum of 
       |(A[0] + A[1] + ... + A[P-1]) - (A[P] + A[P+1] + ... + A[len(A)-1]) | 
       for P in [1, len(A)-1] """
    
    return min(abs(sum(A[:P]) - sum(A[P:])) for P in range(1, len(A)))
