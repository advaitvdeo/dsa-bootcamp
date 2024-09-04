def rotatedBinarySearch(arr, target, start, end):
    # 7, 8, 9, 1, 2, 3, 4, 5
    # target 8
    # https://takeuforward.org/data-structure/search-element-in-a-rotated-sorted-array/

    if start > end:
        return -1

    mid = start + (end - start)//2
    if target == arr[mid]:
        return mid

    # check if left part is sorted
    if arr[start] <= arr[mid]:
        # is target element present in left half
        if target >= arr[start] and target <= arr[mid]:
            return rotatedBinarySearch(arr, target, start, mid-1)
        else:
            return rotatedBinarySearch(arr, target, mid+1, end)
    # it means right part is sorted
    else:
        # is target element present in right part
        if target >= arr[mid] and target <= arr[end]:
            return rotatedBinarySearch(arr, target, mid+1, end)
        else:
            return rotatedBinarySearch(arr, target, start, mid-1)


arr = [7, 8, 9, 1, 2, 3, 4, 5]
target = 8

print(rotatedBinarySearch(arr, target, 0, len(arr)-1))