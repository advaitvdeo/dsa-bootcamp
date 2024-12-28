def helper(arr, index, subset, sum, ans):
    if sum == 0:
        ans.append(subset[:])
        return

    if index >= len(arr):
        return

    if sum < 0:
        return

    myset = set()
    for i in range(index, len(arr)):
        if arr[i] in myset:
            continue
        helper(arr, i + 1, subset + [arr[i]], sum - arr[i], ans)


def combinationSum2(arr, sum):
    ans = []
    arr.sort()
    helper(arr, 0, [], sum, ans)
    return ans


arr = [1, 2, 3, 1]
sum = 5
print(combinationSum2(arr, sum))
