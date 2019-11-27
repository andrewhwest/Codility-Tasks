def missing_value(A):
    """Returns missing integer n from A, where n lies in [1, len(A)+1]"""
    
    B = list(range(1, len(A) + 2))      # Same elements as A but also has missing number  
    
    return min(set(B) - set(A))         # Min returns the value, rather than the set
