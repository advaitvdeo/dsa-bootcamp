def bubbleSort(arr, index):
    if index == len(arr):
        return

    for i in range(len(arr)-index-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    bubbleSort(arr, index+1)


arr = [5, 1, 4, 2, 8]
bubbleSort(arr, 0)
print(arr)