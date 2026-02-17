"""
Docstring for data_generation.generators
"""

def generate_sorted_array(array_size):
    """
    Creates an SORTED array of a size: array_size
    - unsorted array has all elements 1 -> array_size (inclusive)
    
    returns: sorted_array
    """
    return list(range(1, array_size + 1))


if __name__ == "__main__":
    test = generate_sorted_array(100)
    print(test)