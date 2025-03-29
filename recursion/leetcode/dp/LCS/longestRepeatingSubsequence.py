class Solution:
    def longestRepeatingSubsequence_recursive(self, s):
        s1 = s
        s2 = s
        n = m = len(s)
        def solve(n, m):
            if n == 0 or m == 0:
                return 0

            if s1[n-1] == s2[m-1] and n != m:
                return 1 + solve(n-1, m-1)
            else:
                return max(solve(n-1, m), solve(n, m-1))
        return solve(n, m)

    def longestRepeatingSubsequence_memoization(self, s):
        s1 = s2 = s
        n = m = len(s)
        dp = [[-1]*(m+1) for _ in range(m+1)]
        def solve(n, m):
            if n == 0 or m == 0:
                return 0

            if dp[n][m] != -1:
                return dp[n][m]

            if s1[n-1] == s2[m-1] and n != m:
                dp[n][m] = 1 + solve(n-1, m-1)
            else:
                dp[n][m] = max(solve(n-1, m), solve(n, m-1))
            return dp[n][m]
        return solve(n, m)

    def longestRepeatingSubsequence_tabulation(self, s):
        n = m = len(s)
        s1 = s2 = s
        dp = [[-1]*(m+1) for _ in range(n+1)]
        for i in range(m+1):
            dp[0][i] = 0
        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1] and i != j:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]


a = Solution()
s = "AABEBCDD"
print(a.longestRepeatingSubsequence_recursive(s))
print(a.longestRepeatingSubsequence_memoization(s))
print(a.longestRepeatingSubsequence_tabulation(s))