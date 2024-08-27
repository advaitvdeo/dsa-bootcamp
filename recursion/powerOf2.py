def powerOf2(n):
    if n == 1:
        return True

    if n % 2 != 0:
        return False

    return powerOf2(n // 2)


n = 1024
print(powerOf2(n))