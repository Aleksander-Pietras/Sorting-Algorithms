"""
Logic tests for sorting algorithm correctness.

This module ensures that sorting algorithms can produce sorted lists.
Test data is sourced from `data_generators`.

Test Scenarios:
    - Normal Case Testing: ...
    - Stress Testing: Large datasets for stability checks.
"""
import pytest

from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort

@pytest.fixture(params=[bubble_sort, merge_sort])
def sort_function(request):
    return request.param

def test_quantity_stress(sort_function):
    """
    Ensure sort function can be ran multiple times without change; in accuracy and time
    """
    for _ in range(1000):
        sorted_array, unsorted_array = [], [] #TODO: get arrays from data generators
        assert sort_function(unsorted_array) == sorted_array

def test_volume_stress(sort_function):
    """
    Ensure stability when working with large datasets
    """
    sorted_array, unsorted_array = [], [] #TODO: get arrays from data generators
    assert sort_function(unsorted_array) == sorted_array