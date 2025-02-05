"""Module for sorting algorithms"""

import rand

def merge_sort(arr):
    """Fuction merge sorting an array"""
    if len(arr) <= 1:
        return arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    """Function recombining two arrays in order"""
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


curr_arr = rand.random_array([None] * 20)
sorted_arr = bubble_sort(curr_arr)
print("Bubble sorted array is:", sorted_arr)

arr_out = merge_sort(curr_arr)
print("Merge sorted array is:", arr_out)
