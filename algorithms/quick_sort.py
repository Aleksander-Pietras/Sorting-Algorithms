def quick_sort(unsorted_array: list) -> list:
    if len(unsorted_array) <= 1:
        return unsorted_array
    
    pivot_index = len(unsorted_array) // 2 # floor division, picks lower midpoint
    pivot_value = unsorted_array[pivot_index]

    left = []
    middle = []
    right = []

    for num in unsorted_array:
        if num < pivot_value:
            left.append(num)
        elif num == pivot_value:
            middle.append(num)
        else:
            right.append(num)

    return quick_sort(left) + middle + quick_sort(right)

# simple tests
if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(quick_sort(array))

    array2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(quick_sort(array2))