def helper(arr, low, high):
    if low >= high:
        return

    s = low
    e = high
    m = s + (e - s) //2
    pivot = arr[m]

    while s <= e:
        while arr[s] < pivot:
            s += 1
        while arr[e] > pivot:
            e -= 1

        if s <= e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    helper(arr, low, e)
    helper(arr, s, high)


def quickSort(arr):
    helper(arr, 0, len(arr)-1)
    print(arr)


arr = [3, 5, 6, 2, 1, 8]
quickSort(arr)