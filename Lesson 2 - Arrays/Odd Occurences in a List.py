def value_occurences(A):
    """Creates a dictionary of the form {value in A : number of occurences}"""

    value_occurences = {}
    for value in A:
        value_occurences[value] = value_occurences.get(value, 0) + 1
    
    return value_occurences 
    
def unpaired_value(A):
    """Returns the only value that appears once in the list A"""
           
    for value, occurence in value_occurences(A).items():
        if occurence == 1:
            return value
    


