def binarySearch(low, high, arr, target):
    if low > high:
        return -1

    mid = low + (high - low)//2
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return binarySearch(mid+1, high, arr, target)
    else:
        return binarySearch(low, mid-1, arr, target)


arr = [2, 3, 4, 7, 8, 10]
target = 11
print(binarySearch(0, len(arr)-1, arr, target))