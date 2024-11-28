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


def selectionSort3(arr, r, c, max):
    if r == 0:
        return

    if c < r:
        if arr[c] > arr[max]:
            selectionSort3(arr, r, c+1, c)
        else:
            selectionSort3(arr, r, c + 1, max)
    else:
        arr[max], arr[r-1] = arr[r-1], arr[max]
        selectionSort3(arr, r-1, 0, 0)


arr = [25, 64, 12, 22, 11]
#selectionSort(arr, 0)
#print(arr)
#selectionSort2(arr, 0, 1)
#print(arr)
selectionSort3(arr, len(arr), 0, 0)
print(arr)