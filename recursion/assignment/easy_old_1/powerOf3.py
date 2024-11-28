def powerOf3(num):
    if num == 0:
        return False

    if num == 1:
        return True

    if num % 3 == 0:
        return powerOf3(num // 3)
    return False


num = 0
print(powerOf3(num))