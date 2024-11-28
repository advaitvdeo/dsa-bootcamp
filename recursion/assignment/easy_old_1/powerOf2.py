def powerOf2(num):
    if num == 0:
        return False

    if num == 1:
        return True

    if num % 2 == 0:
        return powerOf2(num // 2)
    return False


num = 0
print(powerOf2(num))