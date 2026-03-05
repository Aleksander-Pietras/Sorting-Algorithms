# Testing Strategy

## Goals
- Ensure that all sorting algorithms can pass all the corretness constraints
- Avoid duplication of test logic

### Correctness constrains
Test Scenarios:
* Boundary Cases: Empty lists, single elements.
* Sorted States: Already sorted, reverse sorted, all elements equal.
* Data Varieties: Random integers, random real numbers, negative numbers, and duplicates.
* Stress Testing: Large datasets for stability checks.

## Approach
- pytest used as the test runner
- algorithms injected via fixtures
- each test is ran once for all algorithms

## Current state

Tests created:
- [x] Empty lists
- [x] Single elemtents
- [x] Already sorted
- [x] Reverse sorted
- [x] All elements equal
- [x] Random integers
- [x] Random real numbers (9.dp)
- [x] Negative numbers
- [x] Duplicates
- [ ] Large datasets

Algorithms which passed all the tests:
- [ ] Bubble sort
- [ ] Insertion sort
- [ ] Merge sort
- [ ] Quick sort

## How to run
```python -m pytest tests/test_edge_cases.py```

```python -m pytest tests/test_correctness.py```