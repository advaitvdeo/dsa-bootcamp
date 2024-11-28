def bubbleSort(arr, index):
    if index == 0:
        return

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    bubbleSort(arr, index-1)


arr = [5, 1, 4, 2, 8]
bubbleSort(arr, len(arr)-1)
print(arr)