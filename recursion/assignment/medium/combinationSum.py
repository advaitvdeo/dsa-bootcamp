def combinationSum(candidates, index, target, ds, ans):
    if target == 0:
        ans.append(ds)
        return

    if index == len(candidates):
        return

    if candidates[index] <= target:
        combinationSum(candidates, index, target-candidates[index], ds + [candidates[index]], ans)
    combinationSum(candidates, index+1, target, ds, ans)

candidates = [2]
target = 1
ans = []
combinationSum(candidates, 0, target, [], ans)
print(ans)