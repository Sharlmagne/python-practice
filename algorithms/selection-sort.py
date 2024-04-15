from helper import swap, arr_group


def selection_sort(arr):
    for i in range(len(arr)):
        # Loop from the element next to the current element
        for j in range(i+1, len(arr)):
            # Check if the element of the second loop is greater than the current element of the first loop
            if arr[j] < arr[i]:
                # Swap node if necessary
                swap(j, i, arr)

# Time complexity of O(n^2)


if __name__ == '__main__':
    for array in arr_group:
        print("Unsorted Array:", array)
        selection_sort(array)
        print("Sorted Array:", array)
