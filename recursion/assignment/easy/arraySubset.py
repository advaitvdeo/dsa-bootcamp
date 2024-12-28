def arraySubset(arr, index, ds, ans):
    if index >= len(arr):
        ans += [ds]
        return

    arraySubset(arr, index+1, ds + [arr[index]], ans)
    arraySubset(arr, index+1, ds, ans)


arr = [1, 2, 3]
ans = []
arraySubset(arr, 0, [], ans)
print(ans)