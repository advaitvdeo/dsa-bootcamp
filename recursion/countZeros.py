def countZeros(num):
    if not num:
        return 0

    if not num % 10:
        return 1 + countZeros(num//10)
    return countZeros(num//10)


num = 30201
print(countZeros(num))