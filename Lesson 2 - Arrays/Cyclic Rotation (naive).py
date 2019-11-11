def rotate(A):
    """Shift each element in a list one position to the right"""
    
    *A_except_last, last = A
    rotated_A = [last] + A_except_last
    return rotated_A

def rotate_k_times(A, K):
    """Shifts each element in a list K positions to the right"""

    #Apply rotate(A) K times
    for _ in range(k):
        B = rotate(A)
        A = B
    return A

