def arrayIsSorted(arr, index):
    if index == len(arr)-1:
        return True

    if index < len(arr) - 1:
        return arr[index] <= arr[index+1] and arrayIsSorted(arr, index+1)

#arr = [20, 20, 45, 89, 89, 90]
arr = [20, 20, 78, 98, 99, 97]
print(arrayIsSorted(arr, 0))