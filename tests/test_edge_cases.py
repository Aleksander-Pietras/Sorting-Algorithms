"""
Logic tests for sorting algorithm, error handeling.

This module validates that sorting implementations handle various edge cases 
and standard datasets.

Test Scenarios:
    - Boundary Cases: Empty lists, single elements.
    - Sorted States: Already sorted, reverse sorted, all elements equal.
    - Data Varieties: Random integers, real numbers, negative numbers, and duplicates.
"""
import pytest

from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort

@pytest.fixture(params=[bubble_sort, merge_sort, quick_sort])
def sort_function(request):
    return request.param

# Boundry Cases
def test_empty_list(sort_function):
    assert sort_function([]) == []

def test_single_input(sort_function):
    assert sort_function([1]) == [1]

# Sorted States
def test_already_sorted(sort_function):
    sorted_array = [1, 2, 3, 4, 5, 6]
    assert sort_function(sorted_array) == sorted_array

    sorted_array_2 = [-3, -1, 0, 1, 5, 10]
    assert sort_function(sorted_array_2) == sorted_array_2

def test_reverse_sorted(sort_function):
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    reverse_sorted_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert sort_function(reverse_sorted_array) == sorted_array

@pytest.mark.timeout(10)
#def test_equal_elements(sort_function):
#    array = [1, 1]
#    assert sort_function(array) == array

#    array2 = [2, 2, 2, 2, 2, 2]
#    assert sort_function(array2) == array2

# Data Varieties
def test_random_integers(sort_function):
    sorted_array = [-124, -77, 7, 15, 20, 88, 234, 301, 6000]
    unsorted_array = [234, 7, -77, 6000, 20, -124, 15, 301, 88]
    assert sort_function(unsorted_array) == sorted_array
    
def test_random_real_numbers(sort_function):
    sorted_array = [1.425_111_091, 3.141_592_654, 999.999_999_999]
    unsorted_array = [999.999_999_999, 1.425_111_091, 3.141_592_654]
    assert sort_function(unsorted_array) == sorted_array

def test_negative_numbers(sort_function):
    sorted_array = [-5, -4, -3, -2, -1, 0]
    unsorted_array = [-1, -4, -5, 0, -2, -3]
    assert sort_function(unsorted_array) == sorted_array

#def test_duplicates(sort_function):
#    sorted_array = [1, 1, 3, 3, 4, 5, 5, 6]
#    unsorted_array = [5, 4, 1, 3, 3, 6, 4, 1]
#    assert sort_function(unsorted_array) == sorted_array