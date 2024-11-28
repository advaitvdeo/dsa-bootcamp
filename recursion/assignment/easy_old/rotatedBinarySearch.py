def rotatedBinarySearch(arr, target, s, e):
    if s > e:
        return -1

    m = s + (e-s)//2
    if arr[m] == target:
        return m

    if arr[s] <= arr[m]:
        if target >= arr[s] and target <= arr[m]:
            return rotatedBinarySearch(arr, target, s, m-1)
        else:
            return rotatedBinarySearch(arr, target, m+1, e)

    if target >= arr[m] and target <= arr[e]:
        return rotatedBinarySearch(arr, target, m+1, e)
    else:
        return rotatedBinarySearch(arr, target, s, m-1)


arr = [5, 6, 7, 8, 9, 1, 2, 3]
target = 7
print(rotatedBinarySearch(arr, target, 0, len(arr)-1))