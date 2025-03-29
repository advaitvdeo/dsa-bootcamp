# https://leetcode.com/problems/longest-palindromic-substring/?envType=problem-list-v2&envId=dynamic-programming
"""
Given a string s, return the longest
palindromic

substring
 in s.

"""
class Solution:
    def longestPalindrome(self, s):
        # brute force
        def isPalindrome(i, j):
            while i <= j:
                if dp[i][j] != -1:
                    return dp[i][j]
                if s[i] != s[j]:
                    dp[i][j] = False
                    return False
                i += 1
                j -= 1
            dp[i][j] = True
            return True

        n = len(s)
        ans = ""
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(i, n):
                substr = s[i:j+1]
                if isPalindrome(i, j):
                    if len(substr) > len(ans):
                        ans = substr
        return ans

    def longestPalindrome_neetcode(self, s):
        n = len(s)
        ans = ""
        for i in range(n):
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(ans):
                    ans = s[l:r+1]
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if s[l] == s[r]:
                    if r - l + 1 > len(ans):
                        ans = s[l:r + 1]
                    l -= 1
                    r += 1
        return ans

    def longestPalindrome_dp(self, s):

        s1 = s
        s2 = s[::-1]
        n = m = len(s)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        for i in range(m+1):
            dp[0][i] = 0
        for i in range(n+1):
            dp[i][0] = 0

        ans = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0

                ans = max(ans, dp[i][j])
        print(dp)
        return ans




s = "babad"
a = Solution()
print(a.longestPalindrome(s))
print(a.longestPalindrome_neetcode(s))
print(a.longestPalindrome_dp(s))