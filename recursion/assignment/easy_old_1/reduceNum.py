def reduceNum(num):
    if num == 0:
        return 0

    if num % 2 == 0:
        return 1 + reduceNum(num//2)
    else:
        return 1 + reduceNum(num-1)


num = 14
print(reduceNum(num))