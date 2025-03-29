class Solution:
    def jump(self, nums):
        # recursive solution

        def solve(index):
            if index == len(nums)-1:
                return 0

            if index >= len(nums):
                return float('inf')

            min_jumps = float('inf')
            for i in range(1, min(nums[index]+1, len(nums))):
                jumps = 1 + solve(index + i)
                min_jumps = min(min_jumps, jumps)
            return min_jumps
        return solve(0)

    def jump_dp(self, nums):
        n = len(nums)
        dp = [float('inf')]*n
        dp[n-1] = 0
        for index in range(n-2, -1, -1):
            for i in range(1, min(nums[index]+1, n)):
                jumps = 1 + dp[min(index+i, n-1)]
                dp[index] = min(dp[index], jumps)
        return dp[0]


a = Solution()
nums = [2,3,1,1,4]
print(a.jump(nums))
print(a.jump_dp(nums))