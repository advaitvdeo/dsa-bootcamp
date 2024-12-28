from collections import Counter
class Solution:
    # https://www.youtube.com/watch?v=qhBVWf0YafA
    def permutationUnique(self, nums):
        ans = []
        map = Counter(nums)
        def solve(ds):
            if len(ds) == len(nums):
                ans.append(ds[:])
                return
            for i in map.keys():
                if map[i] > 0:
                    map[i] -= 1
                    solve(ds + [i])
                    map[i] += 1
        solve([])
        return ans

    def permutationUnique2(self, nums):
        ans = []
        visited = [0]*len(nums)
        def solve(ds):
            if len(ds) == len(nums):
                ans.append(ds[:])
                return

            uset = set()
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if nums[i] in uset:
                    continue
                uset.add(nums[i])
                visited[i] = 1
                solve(ds + [nums[i]])
                visited[i] = 0
        solve([])
        return ans

a = Solution()
nums = [1, 2, 3]
nums = [1, 1, 2]
#print(a.permutation(nums))
print(a.permutationUnique2(nums))
