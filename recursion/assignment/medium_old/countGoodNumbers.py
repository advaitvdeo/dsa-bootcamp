def goodNumbers(n, count):
    if n == 1:
        return count + 5

    MOD = 10**9 + 7

    count = 0
    if n % 2 == 0:
        count += 4 * goodNumbers(n-1, count) % MOD
    else:
        count += 5 * goodNumbers(n - 1, count) % MOD

    return count

n = 50
print(goodNumbers(n, 0))