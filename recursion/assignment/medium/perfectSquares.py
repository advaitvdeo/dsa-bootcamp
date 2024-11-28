def perfectSquare(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    min_val = float('inf')
    for i in range(1, n):
        if i*i <= n:
            count = 1 + perfectSquare(n - i*i)
            min_val = min(min_val, count)
    return min_val


n = 14
print(perfectSquare(n))