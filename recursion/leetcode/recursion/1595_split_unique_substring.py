# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/?envType=problem-list-v2&envId=backtracking&difficulty=MEDIUM
"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.
"""
class Solution:
    def maxUniqueSplit(self, s):
        self.max_split = 0
        uset = set()
        def solve(index, curr_split):
            if index >= len(s):
                self.max_split = max(self.max_split, len(curr_split))
                return

            for i in range(index, len(s)):
                substr = s[index:i+1]
                if substr in uset:
                    continue
                uset.add(substr)
                solve(i+1, curr_split + [substr])
                uset.remove(substr)
        solve(0, [])
        return self.max_split


a = Solution()
s = "ababccc"
print(a.maxUniqueSplit(s))