def handshakes(n):
    if n % 2 == 1:
        return 0
    if n == 0:
        return 1

    ans = 0
    for i in range(0, n, 2):
        ans += handshakes(i) * handshakes(n-i-2)

    return ans


n = 8
print(handshakes(n))