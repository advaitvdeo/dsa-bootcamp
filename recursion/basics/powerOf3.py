def powerOf3(n):
    if n == 1:
        return True

    if n % 3 != 0:
        return False

    return powerOf3(n // 3)


n = 81
print(powerOf3(n))