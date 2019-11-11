def minimum_jumps(start, finish, jump_distance):
    """returns the minimum number of jumps to get from start to finish"""
    
    potential_minimum = (finish - start) // jump_distance
    land_on_finish = ((finish - start) % jump_distance) == 0
    
    if land_on_finish:
        return potential_minimum
    else:
        return potential_minimum + 1
    
print(minimal_jumps(23889327489327482370, 832843298743027403247324325, 30))


print(((832843298743027403247324325 - 23889327489327482370) // 30) + 1)

print((832843298743027403247324325 - 23889327489327482370) / 30)