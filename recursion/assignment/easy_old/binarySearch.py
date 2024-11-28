def binarySearch(arr, start, end, target):
    if start > end:
        return -1

    mid = start + (end - start)//2
    if arr[mid] == target:
        return mid

    if target > arr[mid]:
        start = mid + 1
    else:
        end = mid - 1

    return binarySearch(arr, start, end, target)


arr = [-1,0,3,5,9,12]
target = 4
print(binarySearch(arr, 0, len(arr)-1, target))