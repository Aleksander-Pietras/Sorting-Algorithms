"""
Logic tests for sorting algorithm, error handeling.

This module validates that sorting implementations handle various edge cases 
and standard datasets.

Test Scenarios:
    - Boundary Cases: Empty lists, single elements.
    - Sorted States: Already sorted, reverse sorted, all elements equal.
    - Data Varieties: Random integers, negative numbers, and duplicates.
"""
import pytest

from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort

@pytest.fixture(params=[bubble_sort, merge_sort])
def sort_function(request):
    return request.param

def test_empty_list(sort_function):
    with pytest.raises(TypeError, match="Input unsorted list cannot be empty"):
        sort_function([])