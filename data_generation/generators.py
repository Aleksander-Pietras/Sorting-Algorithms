"""
Docstring for data_generation.generators
"""
import random

def generate_sorted_array(array_size):
    """
    Creates an SORTED array of a size: array_size
    - sorted array has all elements 1 -> array_size (inclusive)
    
    :param array_size: Description
    :return: sorted_array
    :rtype: list[int]
    """
    return list(range(1, array_size + 1))

def generate_unsorted_array_efficiently(sorted_array: list[int]):
    """
    Creates an UNSORTED array using a SORTED array. Does NOT create an array in place.
    
    :param sorted_array: Description
    :type sorted_array: list[int]

    :return: unsorted_array
    :rtype: list[int]
    """
    random.shuffle(sorted_array) # sorted_array is not shuffled and random
    return sorted_array

if __name__ == "__main__":
    test = generate_sorted_array(100)
    print(test)