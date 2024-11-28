def countGoodNumbers(n, ans):
    if n == 0:
        return ans

    MOD = 10**9+7
    if n % 2 == 0:
        ans = ((ans % MOD)*5)%MOD
    else:
        ans = ((ans % MOD)*4)%MOD
    return countGoodNumbers(n - 1, ans)

n = 50
print(countGoodNumbers(n, 1))