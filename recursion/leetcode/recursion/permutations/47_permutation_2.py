# https://leetcode.com/problems/permutations-ii/
"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""
from collections import Counter
class Solution:
    # using same solution as permutation, but we are just using an additional check
    # to see if prev char is same as curr char and if we have used prev char
    def permuteUnique(self, nums):
        ans = []
        visited = [0]*len(nums)
        nums.sort()
        def solve(ds):
            if len(ds) == len(nums):
                ans.append(ds[:])
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and visited[i-1]:
                    continue
                if not visited[i]:
                    visited[i] = 1
                    solve(ds + [nums[i]])
                    visited[i] = 0
        solve([])
        return ans

    # another solution is to use a set
    def permuteUnique_set(self ,nums):
        ans = []
        visited = [0]*len(nums)
        def solve(ds):
            if len(ds) == len(nums):
                ans.append(ds[:])
                return

            uset = set()
            for i in range(len(nums)):
                if nums[i] in uset:
                    continue
                if visited[i]:
                    continue
                visited[i] = 1
                uset.add(nums[i])
                solve(ds + [nums[i]])
                visited[i] = 0
        solve([])
        return ans

    def permuteUnique_map(self, nums):
        ans = []
        map = Counter(nums)
        def solve(ds):
            if len(ds) == len(nums):
                ans.append(ds[:])
                return

            for k, v in map.items():
                if v > 0:
                    map[k] -= 1
                    solve(ds + [k])
                    map[k] += 1
        solve([])
        return ans

    def permuteUnique_swap(self, nums):
        ans = []
        def solve(index):
            if index >= len(nums):
                ans.append(nums[:])
                return

            uset = set()
            for i in range(index, len(nums)):
                if nums[i] in uset:
                    continue
                uset.add(nums[i])
                nums[i], nums[index] = nums[index], nums[i]
                solve(index+1)
                nums[i], nums[index] = nums[index], nums[i]
        solve(0)
        return ans

a = Solution()
nums = [1, 2, 2]
print(a.permuteUnique(nums))
print(a.permuteUnique_set(nums))
print(a.permuteUnique_map(nums))
print(a.permuteUnique_swap(nums))