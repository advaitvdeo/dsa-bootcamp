class Solution:
    def coinChange_recursion(self, coins, target):
        n = len(coins)
        def solve(n, target):
            if n == 0:
                if target == 0:
                    return 0
                return float('inf')

            if coins[n-1] <= target:
                return min(1 + solve(n, target - coins[n-1]), solve(n-1, target))
            else:
                return solve(n-1, target)
        return solve(n, target)

    def coinChange_memoization(self, coins, target):
        n = len(coins)
        dp = [[-1]*(target+1) for _ in range(n+1)]
        def solve(n, target):
            if n == 0:
                if target == 0:
                    return 0
                return float('inf')

            if dp[n][target] != -1:
                return dp[n][target]

            if coins[n-1] <= target:
                dp[n][target] = min(1 + solve(n, target - coins[n-1]), solve(n-1, target))
            else:
                dp[n][target] = solve(n-1, target)
            return dp[n][target]

        return solve(n, target)

    def coinChange_tabulation(self, coins, target):
        n = len(coins)
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        for i in range(target+1):
            dp[0][i] = float('inf')
        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            for j in range(1, target+1):
                if coins[i-1] <= j:
                    dp[i][j] = 1 + min(dp[i][j-coins[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]

a = Solution()
coins = [1, 2, 3]
target = 5
print(a.coinChange_recursion(coins, target))
print(a.coinChange_memoization(coins, target))
print(a.coinChange_tabulation(coins, target))
