class Solution:
    def lcstring_recursive(self, x, y):
        n = len(x)
        m = len(y)
        self.ans = 0
        def solve(n, m, len1):
            if n == 0 or m == 0:
                return len1

            if x[n-1] == y[m-1]:
                len1 = solve(n-1, m-1, len1 + 1)

            len2 = solve(n-1, m, 0)
            len3 = solve(n, m-1, 0)

            return max(len1, len2, len3)

        return solve(n, m, 0)

    def lcstring_memoization(self, x, y):
        n = len(x)
        m = len(y)
        self.ans = 0
        dp = [[-1]*(m+1) for _ in range(n+1)]
        def solve(n, m, len1):
            if n == 0 or m == 0:
                return 0

            if dp[n][m] != -1:
                return dp[n][m]

            if x[n - 1] == y[m - 1]:
                dp[n][m] = 1 + solve(n - 1, m - 1, len1)
            else:
                dp[n][m] = 0
            solve(n - 1, m, 0)
            solve(n, m - 1, 0)

            self.ans = max(self.ans, dp[n][m])
            return dp[n][m]

        solve(n, m, 0)
        return self.ans

    def lcstring_tabulation(self, x, y):
        n = len(x)
        m = len(y)
        self.ans = 0
        lcs = ""
        dp = [[-1]*(m+1) for _ in range(n+1)]
        for i in range(m+1):
            dp[0][i] = 0
        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if x[i-1] == y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
                self.ans = max(self.ans, dp[i][j])
        print(lcs)
        return self.ans

a = Solution()
x = "aacabdkacaa"
y = x[::-1]
print(a.lcstring_recursive(x, y))
print(a.lcstring_memoization(x, y))
print(a.lcstring_tabulation(x, y))