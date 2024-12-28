def helper(arr, pos, ans):
    if pos >= len(arr):
        ans.append(arr[:])
        return

    myset = set()
    for i in range(pos, len(arr)):
        if arr[i] in myset:
            continue
        myset.add(arr[i])
        arr[i], arr[pos] = arr[pos], arr[i]
        helper(arr, pos+1, ans)
        arr[i], arr[pos] = arr[pos], arr[i]

def permutationDuplicate(arr):
    ans = []
    helper(arr, 0, ans)
    return ans

arr = [1, 2, 2]
print(permutationDuplicate(arr))