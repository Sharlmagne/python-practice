def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]


def insertion_sort(arr):
    for i in range(1, len(arr)):  # Loop from the second element to the last
        for j in range(i):
            element1 = arr[i - j]
            element2 = arr[i - j - 1]
            #  If the current i element is less than the elements to the left and swap till it is in place.
            if element1 < element2:
                swap(i-j, i-j-1, arr)


if __name__ == '__main__':
    arr = [2, 6, 5, 1, 3, 4]
    arr_2 = [22, 11, 88, 66, 55, 77, 33, 44]
    arr_3 = [11, 9, 29, 7, 2, 15, 28, 7, 7]

    print("Unsorted Array:", arr)
    insertion_sort(arr)
    print("Sorted Array:", arr)
    print("Unsorted Array:", arr_2)
    insertion_sort(arr_2)
    print("Sorted Array:", arr_2)
    print("Unsorted Array:", arr_3)
    insertion_sort(arr_3)
    print("Sorted Array:", arr_3)
