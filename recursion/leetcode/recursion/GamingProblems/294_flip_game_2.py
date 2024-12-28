# https://leetcode.com/problems/flip-game-ii/?envType=problem-list-v2&envId=backtracking&difficulty=MEDIUM
"""
You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return true if the starting player can guarantee a win, and false otherwise.
"""
class Solution:
    def canWin(self, currentState):
        def solve(currentState):
            if "++" not in currentState:
                return False

            for i in range(len(currentState)):
                if currentState[i:i+2] == '++':
                    opponent = solve(currentState[:i]+"--"+currentState[i+2:])
                    if not opponent:
                        return True
            return False
        return solve(currentState)


a = Solution()
currentState = "++++"
print(a.canWin(currentState))