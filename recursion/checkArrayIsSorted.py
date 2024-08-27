def isSorted(arr, index):
    if index == len(arr):
        return True

    if arr[index] >= arr[index-1]:
        return isSorted(arr, index+1)

    return False


arr = [1, 2, 4, 5, 71, 8, 10]
arr = [20, 20, 45, 89, 89, 90]
arr = [20, 20, 78, 98, 99, 97]
print(isSorted(arr, 1))