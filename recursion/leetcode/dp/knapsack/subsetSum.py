# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
"""
Given an array arr[] of non-negative integers and a value sum,
the task is to check if there is a subset of the given array whose sum is equal to the given sum.
"""

class Solution:
    def subsetSum_recursive(self, arr, target):
        def solve(index, sum_val):
            if index >= len(arr):
                if sum_val == target:
                    return True
                return False

            if sum_val > target:
                return False

            return solve(index+1, sum_val + arr[index]) or solve(index+1, sum_val)
        return solve(0, 0)

    def subsetSum_memoization(self, arr, target):
        dp = [[-1 for i in range(target+1)] for j in range(len(arr)+1)]
        def solve(index, sum_val):
            if index >= len(arr):
                if sum_val == target:
                    return True
                return False

            if sum_val > target:
                return False

            if dp[index][sum_val] != -1:
                return dp[index][sum_val]

            dp[index][sum_val] = solve(index+1, sum_val + arr[index]) or solve(index+1, sum_val)
            return dp[index][sum_val]

        return solve(0, 0)

    def subsetSum_topDown(self, arr, target):
        n = len(arr)
        dp = [[-1 for _ in range(target+1)] for _ in range(n+1)]
        for i in range(target+1):
            dp[0][i] = False
        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, target+1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]


arr = [2, 3, 7, 8, 10]
target = 11
a = Solution()
print(a.subsetSum_recursive(arr, target))
print(a.subsetSum_memoization(arr, target))
print(a.subsetSum_topDown(arr, target))