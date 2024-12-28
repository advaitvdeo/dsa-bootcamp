def linearSearch(arr, target, index):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return linearSearch(arr, target, index+1)

arr = [1, 2, 3, 6, 7, 0, 4, 19]
target = -1
print(linearSearch(arr, target, 0))