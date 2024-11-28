def insertionSort(arr, index):
    if index == len(arr):
        return

    for i in range(index):
        if arr[i] > arr[index]:
            temp = arr[index]
            for j in range(index, i, -1):
                arr[j] = arr[j-1]
            arr[i] = temp

    insertionSort(arr, index+1)


arr = [12,11,13,5,6]
arr = [9, 7, 6, 15, 17, 5, 10, 11]
insertionSort(arr, 1)
print(arr)
