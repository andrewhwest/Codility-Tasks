def minimum_difference(A):
    """Returns the minimum tape difference"""
    
    return min(abs(sum(A[:P]) - sum(A[P:])) for P in range(1, len(A)))
