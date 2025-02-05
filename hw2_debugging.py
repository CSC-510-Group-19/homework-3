import rand

def mergeSort(arr):
    if (len(arr) == 1):
        return arr

    half = len(arr)//2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            rightIndex += 1
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        else:
            leftIndex += 1
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + rightIndex] = rightArr[i]
    
    for i in range(leftIndex, len(leftArr)):
        mergeArr[leftIndex + rightIndex] = leftArr[i]

    return mergeArr

def insertion_sort(arr):
    sorted_arr = []
    for i in range(1, len(arr)):
        if not sorted_arr or sorted_arr[-1] <= arr[i]:
            sorted_arr.append(arr[i])
        else:
            for j in range(i, 0, -1):
                sorted_arr.insert(j, arr[j])
    return sorted_arr

arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

insert_sort_arr = insertion_sort(arr)

print(arr_out)
print(insert_sort_arr)


