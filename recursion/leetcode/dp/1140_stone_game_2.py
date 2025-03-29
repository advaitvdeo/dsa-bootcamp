# https://leetcode.com/problems/stone-game-ii/description/
"""
Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get
"""

class Solution:
    def stoneGameII_recursive(self, piles):
        def solve(index, M):
            if index >= len(piles):
                return 0

            curr_sum = 0
            max_sum = float('-inf')
            for i in range(2*M):
                if index + i < len(piles):
                    curr_sum += piles[index+i]
                max_sum = max(max_sum, curr_sum - solve(index+i+1, max(M, i+1)))
            return max_sum
        diff = solve(0, 1)
        sum_val = sum(piles)
        return (sum_val + diff)//2


piles = [2,7,9,4,4]
a = Solution()
print(a.stoneGameII_recursive(piles))

