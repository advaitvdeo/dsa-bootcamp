from math import sqrt
class Solution:
    def getFactors(self, n):
        ans = []
        def solve(number, ds):
            if len(ds) > 1:
                ans.append(ds[:])

            lastFactor = ds.pop()
            if len(ds) == 0:
                start = 2
            else:
                start = ds[-1]
            end = int(sqrt(lastFactor))
            for i in range(start, end+1):
                if lastFactor % i == 0:
                    ds.append(i)
                    ds.append(lastFactor // i)
                    solve(lastFactor // i, ds)
                    ds.pop()
                    ds.pop()
            ds.append(lastFactor)
        solve(n, [n])
        return ans


a = Solution()
n = 32
print(a.getFactors(n))
