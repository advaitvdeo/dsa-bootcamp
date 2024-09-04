def mergeSort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    i = j = k = 0
    sarr = [-1]*(len(left) + len(right))

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sarr[k] = left[i]
            i += 1
        else:
            sarr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        sarr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        sarr[k] = right[j]
        j += 1
        k += 1

    return sarr


def mergeSort2(arr, start, end):
    if end - start == 1:
        return

    mid = (start + end)//2
    mergeSort2(arr, start, mid)
    mergeSort2(arr, mid, end)

    i = start
    j = mid
    k = 0
    sarr = [0]*(end-start)

    while i < mid and j < end:
        if arr[i] < arr[j]:
            sarr[k] = arr[i]
            i += 1
        else:
            sarr[k] = arr[j]
            j += 1
        k += 1
    while i < mid:
        sarr[k] = arr[i]
        i += 1
        k += 1
    while j < end:
        sarr[k] = arr[j]
        j += 1
        k += 1

    for l in range(len(sarr)):
        arr[start+l] = sarr[l]

arr = [3, 5, 2, 6, 7, 22, 16, 89]
#print(mergeSort(arr))
mergeSort2(arr, 0, len(arr))
print(arr)