def earliest_second1(X, A):
    """Returns the smallest index of A such all integers in [1, X] have appeared in A"""
    
    appeared_so_far = set()
    
    for second, position in enumerate(A):

        appeared_so_far.add(position)      # Duplicates aren't added
        
        if len(appeared_so_far) == X:
            return second
        
    return -1
