def factorial(number):
    if not number:
        return 1

    return number * factorial(number-1)


print(factorial(4))