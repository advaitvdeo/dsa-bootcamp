def helper(arr, subset, sum, size, ans):
    if size == 0 and sum == 0:
        ans.append(subset[:])
        return

    if size == 0 or sum == 0:
        return

    if arr > 9:
        return

    helper(arr + 1, subset + [arr], sum - arr, size - 1, ans)
    helper(arr + 1, subset, sum, size, ans)


def combinationSum3(sum, size):
    ans = []
    helper(1, [], sum, size, ans)
    return ans


sum = 6
size = 2
print(combinationSum3(sum, size))