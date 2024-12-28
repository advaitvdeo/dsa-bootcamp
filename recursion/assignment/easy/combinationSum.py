def helper(arr, index, subset, sum, ans):
    if sum == 0:
        ans.append(subset[:])
        return

    if sum < 0:
        return

    if index >= len(arr):
        return

    helper(arr, index, subset + [arr[index]], sum - arr[index], ans)
    helper(arr, index + 1, subset, sum, ans)

def combinationSum(arr, sum):
    arr.sort()
    ans = []
    helper(arr, 0, [], sum, ans)
    return ans


arr = [1, 2, 3]
sum_val = 5
print(combinationSum(arr, sum_val))