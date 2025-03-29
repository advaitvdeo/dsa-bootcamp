class Solution:
    # below one is LCS code only and not superstring code
    # we did not write superstring recursive code
    def printShortestCommonSuperSeq_recursive(self, s1, s2):
        n = len(s1)
        m = len(s2)
        def solve(n, m):
            if n == 0 or m == 0:
                return 0

            if s1[n-1] == s2[m-1]:
                return 1 + solve(n-1, m-1)
            else:
                return max(solve(n-1, m), solve(n, m-1))
        return solve(n, m)

    def printShortestCommonSuperSeq_tabulation(self, s1, s2):
        n = len(s1)
        m = len(s2)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        for i in range(m+1):
            dp[0][i] = 0
        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i = n
        j = m
        ans = ""
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                ans += s1[i-1]
                i -= 1
                j -= 1
            elif dp[i][j-1] > dp[i-1][j]:
                ans += s2[j-1]
                j -= 1
            else:
                ans += s1[i-1]
                i -= 1

        while i > 0:
            ans += s1[i-1]
            i -= 1

        while j > 0:
            ans += s2[j-1]
            j -= 1

        return ans[::-1]


a = Solution()
s1 = "abceft"
s2 = "abdefr"
print(a.printShortestCommonSuperSeq_recursive(s1, s2))
print(a.printShortestCommonSuperSeq_tabulation(s1, s2))