'''
The functions are used to test the algorithms
- This file does not generate the lists, lists are generated at data_generation/generators.py

Correctness tests:
- Empty list
- One element
- Already sorted
- Reverse sorted
- All elements equal
- Random integers
- Negative numbers
- Duplicates
- Large list
'''
import pytest

from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort

@pytest.fixture(params=[bubble_sort, merge_sort])
def sort_function(request):
    return request.param

def test_empty_list(sort_function):
    with pytest.raises(TypeError, match="Input unsorted list cannot be empty"):
        sort_function([])