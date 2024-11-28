def stepsToReduceNumber(number, steps):
    if not number:
        return steps

    if number % 2 == 0:
        return stepsToReduceNumber(number // 2, steps + 1)
    else:
        return stepsToReduceNumber(number - 1, steps + 1)

number = 14
print(stepsToReduceNumber(number, 0))