class Solution:
    def countSubset_recursive(self, arr, target):
        n = len(arr)
        def solve(n, target):
            if n == 0:
                if target == 0:
                    return 1
                return 0

            if target < 0:
                return 0

            return solve(n-1, target - arr[n-1]) + solve(n-1, target)

        return solve(n, target)

    def countSubset_memoization(self, arr, target):
        n = len(arr)
        dp = [[-1]*(target+1) for _ in range(n+1)]

        def solve(n, target):
            if n == 0:
                if target == 0:
                    return 1
                return 0

            if dp[n][target] != -1:
                return dp[n][target]

            if target < 0:
                return 0

            dp[n][target] = solve(n-1, target - arr[n-1]) + solve(n-1, target)
            return dp[n][target]

        return solve(n, target)

    def countSubset_tabulation(self, arr, target):
        n = len(arr)
        dp = [[-1]*(target+1) for _ in range(n+1)]
        for i in range(target+1):
            dp[0][i] = 0
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, target+1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j - arr[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]



a = Solution()
arr = [2, 3, 5, 6, 8, 10]
target = 10
print(a.countSubset_recursive(arr, target))
print(a.countSubset_memoization(arr, target))
print(a.countSubset_tabulation(arr, target))