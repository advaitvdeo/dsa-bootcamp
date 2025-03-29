# https://leetcode.com/problems/integer-break/description/

class Solution:
    def integerBreak_recursive(self, n):
        def solve(num):
            if num <= 3:  # this is because this is the max number that we can get
                return num

            ans = float('-inf')
            for i in range(2, num):
                ans = max(ans, i * solve(num-i))
            return ans

        if n <= 3: # this is because 2 = 1 * 1, 3 = 1 * 2
            return n-1

        return solve(n)

    def integerBreak_memoization(self, n):
        dp = [-1]*(n+1)
        def solve(num):
            if num <= 3:
                return num

            if dp[num] != -1:
                return dp[num]

            ans = float('-inf')
            for i in range(2, num):
                ans = max(ans, i * solve(num-i))
            return ans

        if n <= 3:
            return n-1

        return solve(n)

    def integerBreak_tabulation(self, n):
        if n <= 3:
            return n-1
        dp = [0] * (n + 1)
        for i in range(4):
            dp[i] = i

        for num in range(4, n+1):
            for i in range(2, num):
                dp[num] = max(dp[num], i * dp[num-i])
        return dp[n]


a = Solution()
n = 10
print(a.integerBreak_recursive(n))
print(a.integerBreak_memoization(n))
print(a.integerBreak_tabulation(n))