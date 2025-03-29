# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

"""
Given an integer array arr and an integer difference, return the length of the longest
subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in
the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing
the order of the remaining elements.
"""
from collections import defaultdict
class Solution:
    def longestSubsequence_recursive(self, arr, difference):
        def solve(index):
            result = 0
            for i in range(index+1, len(arr)):
                if arr[i] - arr[index] == difference:
                    result = max(result, 1 + solve(i))
            return result

        result = 0
        for i in range(len(arr)):
            result = max(result, 1 + solve(i))
        return result

    def longestSubsequence_memoization(self, arr, difference):
        n = len(arr)
        dp = [-1]*(n+1)
        def solve(index):
            result = 0
            if dp[index] != -1:
                return dp[index]

            for i in range(index+1, len(arr)):
                if arr[i] - arr[index] == difference:
                    result = max(result, 1 + solve(i))
            dp[index] = result
            return result

        result = 0
        for i in range(len(arr)):
            result = max(result, 1 + solve(i))
        return result

    def longestSubseqeuence_tabulation(self, arr, difference):
        map = defaultdict(int)
        result = 0
        for i in range(len(arr)):
            curr = arr[i]
            prev = arr[i] - difference
            prev_len = map[prev]
            curr_len = prev_len + 1
            map[curr] = curr_len
            result = max(result, curr_len)
        return result


a = Solution()
arr = [1,5,7,8,5,3,4,2,1]
difference = -2
print(a.longestSubsequence_recursive(arr, difference))
print(a.longestSubsequence_memoization(arr, difference))
print(a.longestSubseqeuence_tabulation(arr, difference))