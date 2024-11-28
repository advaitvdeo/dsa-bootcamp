def insertionSort(arr, index):
    if index == len(arr)-1:
        return

    for i in range(index):
        if arr[index] < arr[i]:
            temp = arr[index]
            #for j in range(i, index):
            for j in range(index, i, -1):
                arr[j] = arr[j-1]
            arr[i] = temp
    insertionSort(arr, index+1)


arr = [5, 1, 4, 2, 8]
insertionSort(arr, 0)
print(arr)