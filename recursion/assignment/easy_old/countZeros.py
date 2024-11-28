def countZeros(num):
    if not num:
        return 0

    if num % 10 == 0:
        return 1 + countZeros(num // 10)
    else:
        return countZeros(num // 10)


def countZeros2(num, count):
    if not num:
        return count

    if num % 10 == 0:
        return countZeros2(num // 10, count + 1)
    else:
        return countZeros2(num // 10, count)


num = 30204
print(countZeros(num))
print(countZeros2(num, 0))