def sumOfDigit(num):
    if not num:
        return 0

    return num % 10 + sumOfDigit(num//10)


num = 45632
print(sumOfDigit(num))