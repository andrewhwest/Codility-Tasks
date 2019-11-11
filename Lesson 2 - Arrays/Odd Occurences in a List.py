def value_occurences(A):
    """Creates a dictionary of the form {value in A : number of occurences}"""

    value_occurences = {}
    for value in A:
        value_occurences[value] = value_occurences.get(value, 0) + 1
    
    #value_occurences = {value : sum(1 for x in A if x == value) for value in A} SLOW!!!
    
    return value_occurences 
    
def unpaired_value(A):
    """Returns the only value that appears once in the list A"""
           
    for value, occurence in value_occurences(A).items():
        if occurence == 1:
            return value
    

test = [x for x in range(999500002,1000000000)]
test *= 2
test += [972987]
unpaired_value(test)