def count_occurrences(integer_list):
    """Creates a dictionary of the form {value in A : number of occurrences}, for a list of integers"""

    value_occurrences = {}
    for value in integer_list:
        value_occurrences[value] = value_occurrences.get(value, 0) + 1

    return value_occurrences
 
def unpaired_value(integer_list):
    """Returns the only value that appears once in a list of integers"""

    for value, occurrence in count_occurrences(integer_list).items():
        if occurrence == 1:
            return value
    return False   


