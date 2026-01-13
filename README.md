# Sorting Algorithms

## Contents
- [About This Project](#about-this-project)
- [Design Decisions](#design-decisions)
    - [Algorithms Used](#algorithms-used)
    - [Testing](#testing)
        - [Correctness Tests](#correctness-tests)
        - [Performance Tests](#performance-tests)
- [How to Run](#how-to-run)


## About This Project

In this project, I have independently programmed different sorting algorithms to compare which algorithm performs best in a given situation. 

I have recorded all the tests in ```benchmarks/```

## Design Decisions

### Algortihms Used

The algorithms tested are: bubble sort, merge sort, quick sort, and insertion sort. Additionally, I created my own sorting algorithm to challenge myself before I did further research on other sorting algorithms.
<!--
Make sure to clarify how my sorting algorithm works.
No mystery algorithm!!!
-->

### Testing

To test these algorithms, as well as my programming ability, I have conducted correctness tests and performance tests.

#### Correctness Tests

For the correctness tests, I am testing to check that a given algorithm can sort and handle the following data inputs:

- Empty list
- One element
- Already sorted
- Reverse sorted
- All elements equal
- Random integers
- Negative numbers
- Duplicates
- Large list

These tests check that the data inputs are sorted and that the length of the data inputs is unchanged.

#### Performance Tests

The performance tests measure:

- Time taken
- How time scales with input size
- How input order affects time

For the following data:

- Input sizes: 100, 1k, 5k, 10k, 50k, 100K, 1M
- Input types:
    - Random
    - Already sorted
    - Reverse sorted
    - Nearly sorted

## How to Run

> Instructions will be added once project is complete

<!--
python version
requirements
-->

## Results and Observations

> Results will be added once benchmarking pipeline is finalised