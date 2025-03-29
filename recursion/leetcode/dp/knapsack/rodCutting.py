class Solution:
    def rodCutting_recursive(self, length, price):
        n = len(price)
        def solve(n, L):
            if n == 0 or L == 0:
                return 0

            if length[n-1] <= L:
                return max(price[n-1] + solve(n, L - length[n-1]), solve(n-1, L))
            else:
                return solve(n-1, L)
        return solve(n, n)

    def rodCutting_memoization(self, length, price):
        n = len(price)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        def solve(n, L):
            if n == 0 or L == 0:
                return 0

            if dp[n][L] != -1:
                return dp[n][L]

            if length[n-1] <= L:
                dp[n][L] = max(price[n-1] + solve(n, L - length[n-1]), solve(n-1, L))
            else:
                dp[n][L] = solve(n-1, L)
            return dp[n][L]
        return solve(n, n)

    def rodCutting_tabulation(self, length, price):
        n = len(price)
        L = len(length)
        dp = [[-1]*(L+1) for _ in range(n+1)]
        for i in range(L+1):
            dp[0][i] = 0
        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            for j in range(1, L+1):
                if length[i-1] <= j:
                    dp[i][j] = max(price[i-1] + dp[i][j-length[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][L]


a = Solution()
price = [1, 5, 8, 9, 10, 17, 17, 20]
length = [1, 2, 3, 4, 5, 6, 7, 8]
print(a.rodCutting_recursive(length, price))
print(a.rodCutting_memoization(length, price))
print(a.rodCutting_tabulation(length, price))