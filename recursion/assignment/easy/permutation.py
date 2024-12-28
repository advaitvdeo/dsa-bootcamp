def helper(arr, pos, ans):
    if pos >= len(arr):
        ans.append(arr[:])
        return

    for i in range(pos, len(arr)):
        arr[i], arr[pos] = arr[pos], arr[i]
        helper(arr, pos+1, ans)
        arr[i], arr[pos] = arr[pos], arr[i]

def permutation(arr):
    ans = []
    helper(arr, 0, ans)
    return ans


arr = [1, 2, 3]
print(permutation(arr))

