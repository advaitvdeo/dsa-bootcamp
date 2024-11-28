def binarySearch(arr, target, start, end):
    if start > end:
        return -1

    mid = start + (end - start)//2
    if arr[mid] == target:
        return mid

    if target > arr[mid]:
        start = mid + 1
    if target < arr[mid]:
        end = mid - 1
    return binarySearch(arr, target, start, end)


arr = [-1,0,3,5,9,12]
target = 2
print(binarySearch(arr, target, 0, len(arr)-1))