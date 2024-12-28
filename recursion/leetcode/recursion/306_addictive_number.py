# https://leetcode.com/problems/additive-number/description/?envType=problem-list-v2&envId=backtracking&difficulty=MEDIUM
"""
An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
"""
class Solution:
    def isAdditiveNumber(self, num):
        def solve(index, n1, n2, found):
            if index >= len(num) and found:
                return True

            n3 = str(n1 + n2)
            idx = min(len(num)-index, len(n3))
            if n3 == num[index:index+idx]:
                return solve(index+idx, n2, int(n3), True)
            return False


        for i in range(len(num)-1):
            n1 = int(num[:i+1])
            if str(n1) != num[:i+1]:
                continue
            for j in range(i+1, len(num)):
                n2 = int(num[i+1:j+1])
                if str(n2) != num[i+1:j+1]:
                    continue

                if solve(j+1, n1, n2, False):
                    return True
        return False


a = Solution()
num = "199100199"
num = "11235813"
print(a.isAdditiveNumber(num))