def merge(arr, s, m, e):
    i = s
    j = m
    k = 0
    new_arr = [0] * (e-s)
    while i < m and j < e:
        if arr[i] < arr[j]:
            new_arr[k] = arr[i]
            i += 1
        else:
            new_arr[k] = arr[j]
            j += 1
        k += 1

    while i < m:
        new_arr[k] = arr[i]
        i += 1
        k += 1
    while j < e:
        new_arr[k] = arr[j]
        j += 1
        k += 1

    for l in range(len(new_arr)):
        arr[s+l] = new_arr[l]


def mergeSort(arr, s, e):
    if e - s == 1:
        return

    mid = s + (e - s)//2
    mergeSort(arr, s, mid)
    mergeSort(arr, mid, e)

    merge(arr, s, mid, e)


arr = [3, 5, 6, 2, 1, 8]
mergeSort(arr, 0, len(arr)-1)
print(arr)
