"""Prints out a sorted copy (using merge sort and insertion sort) of a randomly generated array """
import rand

def merge_sort(array):
    """ executes merge sort on array. """
    if len(array) == 1:
        return array

    half = len(array)//2
    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))

def recombine(left_arr, right_arr):
    """recombine is the recombining step of merge sort.

    recombine takes two unsorted arrays and returns them into one sorted array.

    Parameters
    ----------
    left_array : list
        left side of the unsorted array as split in the mergeSort function.
    right_array : list
        right side of the unsorted array as split in the mergeSort function.

    Returns
    -------
    mergeArr : list
        sorted array composed of all values in left_array and right_array.
    """
    left_index = 0
    right_index = 0
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr.append(right_arr[i])

    for i in range(left_index, len(left_arr)):
        merge_arr.append(left_arr[i])

    return merge_arr

def bubble_sort(arr):
    """Fuction bubble sorting an array"""
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Should be `>` for ascending order
                temp = arr[j]  # Incorrect assignment operator
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr  #

def insertion_sort(array):
    """ runs insertion sort on array.

    Parameters
    ----------
    array : list
        array to be sorted.

    Returns
    -------
        sorted copy of list array.
    """

    sorted_arr = []
    for i in range(1, len(array)):
        if not sorted_arr or sorted_arr[-1] <= array[i]:
            sorted_arr.append(array[i])
        else:
            for j in range(i, 0, -1):
                sorted_arr.insert(j, array[j])
    return sorted_arr


curr_arr = rand.random_array([None] * 20)
bubble_arr_out = bubble_sort(curr_arr)
print("Bubble sorted array is:", bubble_arr_out)

arr_out = merge_sort(curr_arr)
print("Merge sorted array is:", arr_out)

arr_out = merge_sort(curr_arr)

insert_sort_arr = insertion_sort(curr_arr)

print(arr_out)
print(insert_sort_arr)
