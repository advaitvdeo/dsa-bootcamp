def powerOfThree(number):
    if number < 3:
        return False

    if number == 3:
        return True

    if number % 3 != 0:
        return False

    return powerOfThree(number // 3)


print(powerOfThree(82))