def rotate(A):
    """Shift each element in a list one position to the right"""
    
    # Move the last element of A to the start
    *A_except_last, last = A
    rotated_A = [last] + A_except_last
    return rotated_A

def rotate_K_times(A, K):
    """Shifts each element in a list K positions to the right"""

    # Apply rotate(A) K times
    for _ in range(K):
        partially_rotated = rotate(A)
        A = partially_rotated
    return A

