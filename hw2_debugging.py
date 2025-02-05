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

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:  # Should be `>` for ascending order
                temp == arr[j]  # Incorrect assignment operator
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr  #


arr = rand.random_array([None] * 20)
sorted_arr = bubble_sort(arr)
print("Bubble sorted array is:", sorted_arr)

arr_out = mergeSort(arr)
print("Merge sorted array is:", arr_out)


