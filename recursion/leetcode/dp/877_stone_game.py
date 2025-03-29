# https://leetcode.com/problems/stone-game/description/
"""
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.
"""
class Solution:
    def stoneGame_recursive(self, piles):
        def solve(i, j):
            if i > j:
                return 0

            left = piles[i] - solve(i+1, j)
            right = piles[j] - solve(i, j-1)

            return max(left, right)
        n = len(piles)
        return solve(0, n-1) > 0

    def stoneGame_memoization(self, piles):
        def solve(i, j):
            if i > j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            left = piles[i] - solve(i+1, j)
            right = piles[j] - solve(i, j-1)

            dp[i][j] = max(left, right)
            return max(left, right)
        n = len(piles)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        return solve(0, n-1) > 0


piles = [5,3,4,5]
a = Solution()
print(a.stoneGame_recursive(piles))
print(a.stoneGame_memoization(piles))