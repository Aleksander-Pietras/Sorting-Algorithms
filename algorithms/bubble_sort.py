def bubble_sort(unsorted_array: list) -> list:
    length = len(unsorted_array)

    passes = -1
    while passes != 0:
        passes = 0

        for i in range(length - 1):
            left = unsorted_array[i]
            right = unsorted_array[i + 1]

            if left >= right:
                unsorted_array[i], unsorted_array[i + 1] = right, left
                passes += 1
            else:
                pass

    return unsorted_array

# simple tests
if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_sort(array))

    array2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_sort(array2))