def selectionSort(arr, pos):
    if pos == len(arr)-1:
        return

    for i in range(pos+1, len(arr)):
        if arr[i] < arr[pos]:
            arr[i], arr[pos] = arr[pos], arr[i]

    selectionSort(arr, pos+1)


def selectionSort2(arr, pos, index):
    if pos >= len(arr)-1:
        return

    if arr[index] < arr[pos]:
        arr[index], arr[pos] = arr[pos], arr[index]
    if index < len(arr) - 1:
        selectionSort2(arr, pos, index+1)
    selectionSort2(arr, pos + 1, pos + 2)


arr = [25, 64, 12, 22, 11]
#selectionSort(arr, 0)
#print(arr)
selectionSort2(arr, 0, 1)
print(arr)