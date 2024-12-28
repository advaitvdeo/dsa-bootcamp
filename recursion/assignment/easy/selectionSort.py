def selectionSort(arr, row, col, maxIndex):
    if row == 0:
        return

    if col < row:
        if arr[col] > arr[maxIndex]:
            maxIndex = col
        selectionSort(arr, row, col+1, maxIndex)
    else:
        arr[row-1], arr[maxIndex] = arr[maxIndex], arr[row-1]
        selectionSort(arr, row-1, 0, 0)


arr = [3, 5, 6, 2, 1, 8]
selectionSort(arr, len(arr), 0, 0)
print(arr)