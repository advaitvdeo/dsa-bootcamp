def quickSort(arr, low, high):
    if low >= high:
        return

    start = low
    end = high
    mid = start + (end - start)//2

    pivot = arr[mid]
    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1

        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    quickSort(arr, low, end)
    quickSort(arr, start, high)


arr = [3, 5, 2, 6, 7, 22, 16, 89]
quickSort(arr, 0, len(arr)-1)
print(arr)