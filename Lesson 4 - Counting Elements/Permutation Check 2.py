def permutation_check_version2(A):
    """Returns 1 if A only contains every integer in [1, len(A)], 0 if not"""
    
    A.sort()
    if A == list(range(1, len(A)+1)):
        return 1
    else:
        return 0

