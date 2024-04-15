def linear_search(arr, search_value):
    for index, element in enumerate(arr):
        if element == search_value:
            return index

"""
Sort the list of values
Determine the center of the array
Determine if the search value is greater, less or equal to the value at the center of the array
Reduce the size of the array to the size where the search value is likely at
Continue until the left array is size of one or until the value is equal to value at the center of the array
"""


def binary_search(arr, search_value):
    left_index = 0
    right_index = len(arr) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = arr[mid_index]

        if search_value == mid_number:
            return mid_index
        elif search_value > mid_number:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


def binary_search_recursion(arr, search_value, left_index: None, right_index: None):
    # Handle error if value is not in arr.
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(arr) or mid_index < 0:
        return -1  # Handle error if the mid_index is out of bounds
    mid_number = arr[mid_index]

    if search_value == mid_number:
        return mid_index
    elif search_value > mid_number:
        left_index = mid_index + 1
    elif search_value < mid_number:
        right_index = mid_index - 1

    return binary_search_recursion(arr, search_value, left_index, right_index)


if __name__ == "__main__":
    arr = [12, 15, 17, 19, 21, 24, 45, 67]
    search_value = 19


    index = linear_search(arr, search_value)
    print(f"Number found at index {index} using linear search.")

    index_2 = binary_search(arr, search_value)
    print(f"Number found at index {index_2} using binary search.")

    index_3 = binary_search_recursion(arr, search_value, 0, len(arr)-1)
    print(f"Number found at index {index_3} using binary search.")