def combinationSum(candidates, target, ds, ans, index):
    if target == 0:
        ans.append(ds[:])
        return

    if index == len(candidates):
        return

    if candidates[index] <= target:
        # pick the element
        combinationSum(candidates, target - candidates[index], ds + [candidates[index]], ans, index)
    combinationSum(candidates, target, ds, ans, index + 1)


ans = []
candidates = [2,3,6,7]
candidates = [2,3,5]
target = 7
target = 8
combinationSum(candidates, target, [], ans, 0)
print(ans)