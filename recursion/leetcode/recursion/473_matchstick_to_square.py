# https://leetcode.com/problems/matchsticks-to-square/description/?envType=problem-list-v2&envId=backtracking&difficulty=MEDIUM
"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick.
You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each
matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.
"""
class Solution:
    def makesquare(self, matchsticks):
        visited = [0] * len(matchsticks)
        target = sum(matchsticks) // 4
        if target * 4 != sum(matchsticks):
            return False
        def solve(index, curr_sum, target, sides):
            if sides == 4:
                return True

            if curr_sum == target:
                return solve(0, 0, target, sides+1)

            if curr_sum > target:
                return False

            for i in range(index, len(matchsticks)):
                if not visited[i]:
                    visited[i] = 1
                    if solve(i+1, curr_sum + matchsticks[i], target, sides):
                        return True
                    visited[i] = 0
            return False
        return solve(0, 0, target, 0)

a = Solution()
matchsticks = [1,1,2,2,2]
matchsticks = [3,3,3,3,4]
print(a.makesquare(matchsticks))