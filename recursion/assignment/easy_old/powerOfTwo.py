def powerOfTwo(number):
    if number == 1:
        return True

    if number == 0:
        return False

    if number % 2 != 0:
        return False

    return powerOfTwo(number // 2)


print(powerOfTwo(0))