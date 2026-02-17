"""
Docstring for data_generation.generators
"""
import random

def generate_sorted_array(array_size: int) -> list[int]:
    """
    Creates an SORTED array of a size: array_size + 1
    - sorted array has all elements 1 -> array_size (inclusive)
    
    :param array_size: The max value in the array. Also determines the length of the array.
    :type array_size: int
    :return: sorted_array
    :rtype: list[int]
    """
    return list(range(1, array_size + 1))

def generate_unsorted_array_efficiently(sorted_array: list[int]) -> list[int]:
    """
    Creates an UNSORTED array using a SORTED array. Does NOT create an array in place.
    
    :param sorted_array: Array of intigers, in order, length: array_size + 1, with min: 1, and max: array_size. No duplicate values.
    :type sorted_array: list[int]
    :return: unsorted_array
    :rtype: list[int]
    """
    random.shuffle(sorted_array) # sorted_array is not shuffled and random
    return sorted_array

def generate_unsorted_array_(array_size: int) -> list[int]:
    """
    Creates an USORTED array of size: array_size + 1
    
    :param array_size: The max value in the array. Also determines the length of the array.
    :type array_size: int
    :return: unsorted_array
    :rtype: list[int]
    """
    array = list(range(1, array_size + 1))
    random.shuffle(array)
    return array

def fetch_arrays_for_testing(array_size: int):
    """
    Fetches sorted array and unsorted array, respectfully. Returns 2 items.
    
    :param array_size: The max value in the array. Also determines the length of the array
    :type array_size: int
    """
    sorted_array = generate_sorted_array(array_size)
    unsorted_array = sorted_array.copy() # shuffle works in place
    unsorted_array = generate_unsorted_array_efficiently(unsorted_array)

    return sorted_array, unsorted_array

if __name__ == "__main__":
    test = fetch_arrays_for_testing(100)
    print(test)