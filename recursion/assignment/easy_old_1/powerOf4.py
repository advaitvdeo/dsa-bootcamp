def powerOf4(num):
    if num == 0:
        return False

    if num == 1:
        return True

    if num % 4 == 0:
        return powerOf4(num // 4)

    return False


num = 20
print(powerOf4(num))