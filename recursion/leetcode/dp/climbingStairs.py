# https://www.youtube.com/watch?v=S31W3kohFDk&list=PLDzeHZWIZsTomOPnCiU3J95WufjE36wsb&index=2
class Solution:
    def climbingStairs(self, n):
        def solve(index):
            if index >= n:
                return 1

            return solve(index+1) + solve(index+2)
        return solve(0)


a = Solution()
n = 3
print(a.climbingStairs(n))