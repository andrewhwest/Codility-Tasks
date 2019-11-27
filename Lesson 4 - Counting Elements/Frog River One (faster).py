def earliest_second_version2(X, A):
    """Returns the smallest index of A such all integers in [1, X] have appeared in A"""
    
    appeared_so_far = set()

    for second, position in enumerate(A):
        
        # Avoid checking to see if we have finished early on
        if (second < X) and position not in appeared_so_far:
            appeared_so_far.add(position)
            continue
        
        # Now check each time a new element is added to the set
        if position not in appeared_so_far:
            appeared_so_far.add(position)
            if len(appeared_so_far) == X:
                return second
    
    # Only arrive here if we haven't found every integer we need
    return -1
