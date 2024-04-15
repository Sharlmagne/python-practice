from insertion_sort import insertion_sort, swap


def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while arr[j - gap] > anchor and j >= gap:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap //= 2


if __name__ == '__main__':
    arr = [2, 6, 5, 1, 3, 4]
    arr_2 = [22, 11, 88, 66, 55, 77, 33, 44]
    arr_3 = [11, 9, 29, 7, 2, 15, 28, 7, 7]
    arr_4 = [21, 38, 29, 17, 4, 25, 11, 32, 9]

    shell_sort(arr_4)
    print(arr_4)

    # print("Unsorted Array:", arr)
    # insertion_sort(arr)
    # print("Sorted Array:", arr)
    # print("Unsorted Array:", arr_2)
    # insertion_sort(arr_2)
    # print("Sorted Array:", arr_2)
    # print("Unsorted Array:", arr_3)
    # insertion_sort(arr_3)
    # print("Sorted Array:", arr_3)