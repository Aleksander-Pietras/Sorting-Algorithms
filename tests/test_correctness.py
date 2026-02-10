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
