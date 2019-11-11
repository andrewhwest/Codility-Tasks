def minimum_jumps(start, finish, jump_distance):
    """Returns the minimum number of jumps to get from start to finish"""
    
    potential_minimum = (finish - start) // jump_distance
    land_on_finish = ((finish - start) % jump_distance) == 0
    
    if land_on_finish:
        return potential_minimum
    else:
        return potential_minimum + 1
    
