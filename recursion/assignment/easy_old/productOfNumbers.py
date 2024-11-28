def productOfNumbers(num1, num2):
    if not num2:
        return 0

    return num1 + productOfNumbers(num1, num2-1)


print(productOfNumbers(10, 15))