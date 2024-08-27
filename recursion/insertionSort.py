def insertionSort(arr, index):
    if index == len(arr):
        return

    for i in range(index):
        if arr[i] > arr[index]:
            index_val = arr[index]
            for j in range(index, i, -1):
                arr[j] = arr[j-1]
            arr[i] = index_val

    insertionSort(arr, index+1)


arr = [5, 1, 4, 2, 8, 3, 66, 90, 87, 54]
insertionSort(arr, 1)
print(arr)

