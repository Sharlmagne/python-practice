"""
Partition the array so that the pivot has smaller values on the left and larger values on the right
Select the last element to be the pivot
Create a pointer for the beginning of the array and up to the node beside the pivot
For the left most pointer, move it until it lands on an element greater than the pivot
For the right most pointer, move it until it lands on an element less than the pivot
Check if the right most pointer reaches or passes the left most pointer
If the pointers does not overlap, swap the values
If the pointers overlap, swap the left pointer value with the pivot value, and the pivot will be in place
Return the index for the pivot
Call a function to recursively partition both sides of the pivot

"""


def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]



def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]  # Use the last element of the array as the pivot

    while i < j:  # Continue looping as long as the indexes does not pass each other
        while i < right:  # Loops until the value of the element at the right index is greater that the pivot
            if arr[i] > pivot:
                break
            i += 1
        while j > left:  # Loops until the value of the element at the left index is less that the pivot
            if arr[j] < pivot:
                break
            j -= 1
        if i > j:  # Check if the right or left index crosses each other and break the loop
            break
        if arr[i] > pivot > arr[j]:
            swap(i, j, arr)
    if arr[i] > pivot:
        swap(i, right, arr)  # Swap the value at the right index with the value at the pivot
    return i


def quick_sort(arr, left, right):
    if left < right:  # Checks if the right index goes beyond the left index and stops the recursion
        index = partition(arr, left, right)
        quick_sort(arr, left, index - 1)  # Recursively call the function on the right side of the array
        quick_sort(arr, index + 1, right)  # Recursively call the function on the left side of the array


if __name__ == "__main__":
    arr = [22, 11, 88, 66, 55, 77, 33, 44]
    arr_2 = [11, 9, 29, 7, 2, 15, 28, 7, 7]

    print("Original:", arr)
    quick_sort(arr, 0, (len(arr)-1))
    print("Sorted:", arr)

    print("Original:", arr_2)
    quick_sort(arr_2, 0, (len(arr_2) - 1))
    print("Sorted:", arr_2)