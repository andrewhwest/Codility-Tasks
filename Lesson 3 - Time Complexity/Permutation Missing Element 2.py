def missing_value2(A):
    """Returns missing integer n from A, where n lies in [1, len(A)+1]"""
    
    sorted_A = A.sort()
    missing = min(y for x,y in zip(A[1:], A) if x - y == 2) 
    
    return missing + 1