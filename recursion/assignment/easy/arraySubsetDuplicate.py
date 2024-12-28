def arraySubsetDuplicate(arr, index, ds, ans):
    if index >= len(arr):
        ans += [ds]
        return

    arraySubsetDuplicate(arr, index+1, ds + [arr[index]], ans)
    while index < len(arr) - 1 and arr[index] == arr[index+1]:
        index += 1
    arraySubsetDuplicate(arr, index+1, ds, ans)


arr = [1, 2, 2]
ans = []
arraySubsetDuplicate(arr, 0, [], ans)
print(ans)