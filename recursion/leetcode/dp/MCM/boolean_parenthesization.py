from collections import defaultdict
class Solution:
    def boolean_parenthesization(self, s):
        n = len(s)
        map = defaultdict(bool)
        def solve(i, j, isTrue):
            if i > j:
                return False

            if i == j:
                if isTrue:
                    return s[i] == 'T'
                else:
                    return s[i] == 'F'

            if f"{i}-{j}-{isTrue}" in map:
                return map[f"{i}-{j}-{isTrue}"]

            ans = 0
            for k in range(i+1, j, 2):
                lt = solve(i, k-1, True)
                lf = solve(i, k-1, False)
                rt = solve(k+1, j, True)
                rf = solve(k+1, j, False)

                if s[k] == '&':
                    if isTrue:
                        ans += lt * rt
                    else:
                        ans += lf * rt + lt * rf + lf * rf
                elif s[k] == '|':
                    if isTrue:
                        ans += lt * rf + lf * rt + lt * rt
                    else:
                        ans += lf * rf
                elif s[k] == '^':
                    if isTrue:
                        ans += lt * rf + rt * lf
                    else:
                        ans += lt * rt + lf * rf
            map[f"{i}-{j}-{isTrue}"] = ans
            return ans
        return solve(0, n-1, True)

a = Solution()
s = 'T|F&T^F'
print(a.boolean_parenthesization(s))