def rotate_K_times(A, K):
    """shift each element in a list of numbers A, K positions to the right"""
    
    INDEX_INCREASE = K % len(A)                  
    SLICE_INDEX = len(A) - INDEX_INCREASE
    #Every element with index >= SLICE_INDEX moves to the start of the rotated list
    
    return A[SLICE_INDEX:] + A[:SLICE_INDEX]        

tester = [x for x in range(1000)]
rotate_K_times([3,8,9,7,6], 3)
