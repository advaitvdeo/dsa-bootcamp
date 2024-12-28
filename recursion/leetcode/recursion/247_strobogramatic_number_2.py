# https://leetcode.com/problems/strobogrammatic-number-ii/description/?envType=problem-list-v2&envId=recursion&favoriteSlug=&difficulty=MEDIUM

"""
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
"""

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        reversiblePairs = {"1": "1", "6": "9", "8": "8", "9": "6", "0": "0"}
        def generateStroboNumbers(n, finalLength):
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]

            prev_strobo_nums = generateStroboNumbers(n-2, finalLength)
            curr_strobo_nums = []

            for prev_strobo_num in prev_strobo_nums:
                for k, v in reversiblePairs.items():
                    if k != '0' or n != finalLength:
                        curr_strobo_nums.append(k + prev_strobo_num + v)

            return curr_strobo_nums
        return generateStroboNumbers(n, n)


a = Solution()
n = 3
print(a.findStrobogrammatic(n))
