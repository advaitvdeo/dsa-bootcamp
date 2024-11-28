def pow(x, ans, n):
    if not n:
        return ans

    if n < 0:
        ans /= x
        return pow(x, ans, n + 1)
    else:
        ans *= x
        return pow(x, ans, n - 1)


print(pow(2.1, 1, 10))