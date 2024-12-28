# https://leetcode.com/problems/permutations/description/?envType=problem-list-v2&envId=backtracking&difficulty=MEDIUM
"""
Given an array nums of distinct integers, return all the possible
permutations
. You can return the answer in any order.
"""
class Solution:
    def permute(self, nums):
        # using recursion
        ans = []
        visited = [0]*len(nums)
        def solve(ds):
            if len(ds) == len(nums):
               ans.append(ds[:])
               return

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = 1
                    solve(ds + [nums[i]])
                    visited[i] = 0
        solve([])
        return ans

a = Solution()
nums = [1, 2, 3]
print(a.permute(nums))