def sumOfDigit(number):
    if not number:
        return 0

    return number % 10 + sumOfDigit(number//10)


number = 123123
print(sumOfDigit(number))