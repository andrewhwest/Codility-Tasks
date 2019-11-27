def permutation_check(A):
    """Returns 1 if A only contains every integer in [1, len(A)], 0 if not"""
    
    B = set(list(range(1, len(A)+1)))
    A_has_correct_elements = (set(A) == set(B))
    
    if A_has_correct_elements:
        return 1
    else:
        return 0
