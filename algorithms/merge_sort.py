def merge_sort(unsorted_array: list) -> list:
    length = len(unsorted_array)
    if length <= 1:
        return unsorted_array
    
    left_side, right_side = divide(unsorted_array, length)

    sorted_array = conquer(left_side, right_side)
    return sorted_array

def divide(unsorted_array: list, length: int):
    if length % 2 != 0:
        left_half = (length / 2) + 0.5
        right_half = (length / 2) + 0.5
    else:
        left_half = length / 2
        right_half = length / 2
    
    left_side = unsorted_array[:int(left_half)]
    right_side = unsorted_array[int(right_half):]

    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)

    return left_side, right_side

def conquer(left_side: list, right_side: list):
    sorted_array = []
    
    left_length = len(left_side)
    right_length = len(right_side)

    i = 0
    j = 0

    while i < left_length and j < right_length:
        if left_side[i] <= right_side[j]:
            sorted_array.append(left_side[i])
            i += 1
        else:
            sorted_array.append(right_side[j])
            j += 1

    # append remaining elements
    while i < left_length:
        sorted_array.append(left_side[i])
        i += 1

    while j < right_length:
        sorted_array.append(right_side[j])
        j += 1

    return sorted_array

# simple tests
if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(merge_sort(array))

    array2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(merge_sort(array2))