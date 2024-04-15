def bubble_sort1(arr):
    # swapped = False

    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1 - i):
            # Subtracting i prevents the iteration from going to the end everytime
            element1 = arr[j]
            element2 = arr[j + 1]
            if element1 > element2:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap variables
                swapped = True
        if not swapped:  # If the list is already sorted, the loop will break after first loop.
            break


def bubble_sort2(arr, key):
    swapped = False
    arr_length = len(arr)
    for i in range(arr_length):
        for j in range(arr_length - 1 - i):  # Subtracting i prevents the iteration from going to the end everytime
            if arr[j][key] > arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap variables
                swapped = True
        if not swapped:  # If the list is already sorted, the loop will break after first loop.
            break


if __name__ == "__main__":
    arr = [5, 9, 2, 1, 67, 34, 88, 34]
    sorted_arr = [1, 2, 5, 9, 34, 34, 67, 88]
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    print("Unsorted Array:", arr)
    bubble_sort1(arr)
    print("Sorted Array:", arr)

    print("Unsorted Array:", elements)
    bubble_sort2(elements, "transaction_amount")
    print("Sorted Array:", elements)
