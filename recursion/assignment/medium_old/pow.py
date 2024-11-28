def power(x, n):
    if n == 0:
        return 1.0

    if n < 0:
        return 1 / (float(x)) * power(x, n + 1)
    return float(x) * power(x, n-1)


print(power(10, -3))