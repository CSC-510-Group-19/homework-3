"""Prints out a sorted copy (using merge sort and insertion sort) of a randomly generated array """
import rand


def merge_sort(array):
    """ executes merge sort on array. """
    if len(array) == 1:
        return array

    half = len(array)//2

    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))

def recombine(left_array, right_array):
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
    merge_array = [None] * (len(left_array) + len(right_array))
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            right_index += 1
            merge_array[left_index + right_index] = left_array[left_index]
        else:
            left_index += 1
            merge_array[left_index + right_index] = right_array[right_index]

    for i in range(right_index, len(right_array)):
        merge_array[left_index + right_index] = right_array[i]

    for i in range(left_index, len(left_array)):
        merge_array[left_index + right_index] = left_array[i]

    return merge_array

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

arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

insert_sort_arr = insertion_sort(arr)

print(arr_out)
print(insert_sort_arr)

