def arrayIsSorted(arr):
    if len(arr) <= 1:
        return True

    if arr[0] > arr[1]:
        return False

    return arrayIsSorted(arr[1:])


arr = [20, 21, 45, 89, 89, 90]
arr = [20, 20, 78, 98, 99, 97]
print(arrayIsSorted(arr))