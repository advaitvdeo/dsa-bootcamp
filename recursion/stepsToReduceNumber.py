def stepsToReduceNumber(num):
    if num == 0:
        return 0

    if num % 2 != 0:
        return 1 + stepsToReduceNumber(num - 1)
    else:
        return 1 + stepsToReduceNumber(num // 2)


num = 123
print(stepsToReduceNumber(num))