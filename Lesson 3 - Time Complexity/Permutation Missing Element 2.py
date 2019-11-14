def missing_value2(A):
    """Returns missing integer n from A, where n lies in [1, len(A)+1]"""
    
    A.sort()
    #look for a difference of 2 between adjacent values in sorted A
    value_before_missing = min(y for x,y in zip(A[1:], A) if x - y == 2) 
    
    return value_before_missing + 1
