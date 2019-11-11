def rotate(A):
    """shift each element in a list one position to the right"""
    
    *A_except_last, last = A
    rotated_A = [last] + A_except_last
    return rotated_A

def rotate_k_times(A, k):
    
    for _ in range(k):
        B = rotate(A)
        A = B
    return A

rotate_k_times([1,2,3,4], 10001)