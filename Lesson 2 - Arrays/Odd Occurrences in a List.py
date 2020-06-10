def count_occurrences(A):
    """Creates a dictionary of the form {value in A : number of occurrences}, for a list of integers A"""

    value_occurrences = {}
    for value in A:
        value_occurrences[value] = value_occurrences.get(value, 0) + 1
    
    return value_occurrences 
    
def unpaired_value(A):
    """Returns the only value that appears once in the list A"""
           
    for value, occurrence in count_occurrences(A).items():
        if occurrence == 1:
            return value
    


