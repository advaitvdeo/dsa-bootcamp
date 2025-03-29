class Solution:
    def printLCS_recursive(self, x, y):
        n = len(x)
        m = len(y)
        lcs = ""
        def solve(n, m):
            if n == 0 or m == 0:
                return 0

            if x[n-1] == y[m-1]:
                return 1 + solve(n-1, m-1)
            else:
                return max( solve(n-1, m), solve(n, m-1))
        return solve(n, m)

    def printLCS_tabulation(self, x, y):
        n = len(x)
        m = len(y)
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
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # i = n
        # j = m
        # ans = ""
        # while i >= 0 and j >= 0:
        #     if x[i-1] == y[j-1]:
        #         ans += x[i-1]
        #         i -= 1
        #         j -= 1
        #     elif dp[i-1][j] > dp[i][j-1]:
        #         i -= 1
        #     else:
        #         j -= 1
        # return ans[::-1]

        last_arr = dp[-1]
        ans = ""
        for i in range(len(last_arr)-1):
            if last_arr[i] != last_arr[i+1]:
                ans += y[i]
        return ans



a = Solution()
x = "abcfh"
y = "abdchg"

x = "abceft"
y = "abdefr"
print(a.printLCS_recursive(x, y))
print(a.printLCS_tabulation(x, y))