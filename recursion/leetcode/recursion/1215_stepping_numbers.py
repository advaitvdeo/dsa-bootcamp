# https://leetcode.com/problems/stepping-numbers/description/?envType=problem-list-v2&envId=backtracking&difficulty=MEDIUM
"""
A stepping number is an integer such that all of its adjacent digits have an absolute difference of exactly 1.

For example, 321 is a stepping number while 421 is not.
Given two integers low and high, return a sorted list of all the stepping numbers in the inclusive range [low, high].
"""
class Solution:
    def countSteppingNumbers(self, low, high):

        def solve(num):
            if num >= low and num <= high:
                ans.append(num)

            if num < high:
                last_digit = num % 10
                if last_digit > 0:
                    solve(num * 10 + last_digit - 1)
                if last_digit < 9:
                    solve(num * 10 + last_digit + 1)

        ans = []
        if low == 0:
            ans.append(low)
        for i in range(1, 10):
            solve(i)
        return ans


a = Solution()
low = 10
high = 88
print(a.countSteppingNumbers(low, high))