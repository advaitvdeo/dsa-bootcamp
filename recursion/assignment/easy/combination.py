def helper(arr, index, k, subset, ans):
    if k == 0:
        ans.append(subset[:])
        return
    if index >= len(arr):
        return
    if k > len(arr) - index + 1:
        return
    helper(arr, index+1, k-1, subset + [arr[index]], ans)
    helper(arr, index+1, k, subset, ans)

def combination(arr, k):
    ans = []
    helper(arr, 0, k, [], ans)
    return ans

arr = [1, 2, 3, 4, 5]
k = 3
print(combination(arr, k))