"""
Create a function to split an array in two
Create a function to sort merge two arrays into one
Recursively split the function then sort and merge until the array is fully sorted
"""

# Take values from two different arrays and sort and merge them into one array
def merge(a, b, arr):
    i = 0
    while len(a) != 0 or len(b) != 0:
        if len(a) == 0:
            arr[i] = b.pop(0)
            i += 1
        elif len(b) == 0:
            arr[i] = a.pop(0)
            i += 1
        elif a[0] < b[0]:
            arr[i] = a.pop(0)
            i += 1
        elif b[0] < a[0]:
            arr[i] = b.pop(0)
            i += 1
        elif a[0] == b[0]:
            arr[i] = a.pop(0)
            i += 1


def split(arr):
    split_index = len(arr) // 2
    arr1 = arr[0:split_index]
    arr2 = arr[split_index:]
    return arr1, arr2


def merge_sort(arr):
    if len(arr) > 1:
        arr1, arr2 = split(arr)
        merge_sort(arr1)
        merge_sort(arr2)
        merge(arr1, arr2, arr)


if __name__ == '__main__':
    arr = [2, 6, 5, 1, 7, 4, 3]
    arr_2 = []
    arr_3 = [2, 2]
    arr_4 = [0]
    arr_5 = [1, 2, 4, 3, 2, 1, 9, 6, 7, 5, 3]
    arr_group = [arr, arr_2, arr_3, arr_4, arr_5]

    for array in arr_group:
        merge_sort(array)
        print(array)


