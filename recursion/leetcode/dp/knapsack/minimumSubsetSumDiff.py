class Solution:
    def minimumSubsetSumDiff(self, arr):
        n = len(arr)
        self.min_diff = sum(arr)
        def solve(n, curr_sum):
            if n == 0:
                self.min_diff = min(self.min_diff, abs(sum(arr) - curr_sum*2))
                return

            solve(n-1, curr_sum + arr[n-1])
            solve(n-1, curr_sum)

        solve(n, 0)
        return self.min_diff

    def minimumSubsetSumDiff_memoization(self, arr):
        n = len(arr)
        self.min_diff = sum(arr)
        dp = [[-1]*(sum(arr)+1) for _ in range(n+1)]

        def solve(n, curr_sum, min_diff):
            if n == 0:
                return min(min_diff, abs(sum(arr) - 2*curr_sum))

            if dp[n][curr_sum] != -1:
                return dp[n][curr_sum]

            pick = solve(n - 1, curr_sum + arr[n - 1], min_diff)
            not_pick = solve(n - 1, curr_sum, min_diff)

            dp[n][curr_sum] = min(pick, not_pick)
            return dp[n][curr_sum]

        return solve(n, 0, float('inf'))

    def minimumSubsetSumDiff_tabluation(self, arr):
        n = len(arr)
        target = sum(arr)
        dp = [[-1]*(target+1) for _ in range(n+1)]
        for i in range(target+1):
            dp[0][i] = False
        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, target+1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        v = []
        for i in range(len(dp[-1])//2):
            if dp[-1][i]:
                v.append(i)
        min_val = float('inf')
        for val in v:
            min_val = min(min_val, sum(arr) - 2*val)
        return min_val


    def minimumSubsetSumDiff_av(self, arr):
        n = len(arr)
        target = sum(arr)
        dp = [[-1]*(target+1) for _ in range(n+1)]
        for i in range(1, target+1):
            dp[0][i] = False
        for i in range(1, n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, target+1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        v = []
        for i in range((target+1)//2):
            if dp[n][i]:
                v.append(i)
        min_diff = float('inf')
        for val in v:
            min_diff = min(min_diff, sum(arr)-2*val)
        return min_diff



a = Solution()
arr = [1, 5, 6, 11]
print(a.minimumSubsetSumDiff(arr))
print(a.minimumSubsetSumDiff_memoization(arr))
print(a.minimumSubsetSumDiff_tabluation(arr))
print(a.minimumSubsetSumDiff_av(arr))