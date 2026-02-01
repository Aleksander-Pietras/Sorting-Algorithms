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
- [ ] Single elemtents
- [ ] Already sorted
- [ ] Reverse sorted
- [ ] All elements equal
- [ ] Random integers
- [ ] Random real numbers (9.dp)
- [ ] Negative numbers
- [ ] Duplicates
- [ ] Large datasets

Algorithms which passed the tests:
- [ ] Bubble sort
- [ ] Insertion sort
- [ ] Merge sort
- [ ] Quick sort