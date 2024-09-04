def binarySearch(arr, target, start, end):
    if start > end:
        return -1

    mid = start + (end - start)//2
    if target == arr[mid]:
        return mid
    if target > arr[mid]:
        return binarySearch(arr, target, mid + 1, end)
    return binarySearch(arr, target, start, mid-1)


arr = [1, 2, 4, 66, 78, 99]
start = 0
end = len(arr)-1
target = 1
ans = binarySearch(arr, target, start, end)
print(ans)