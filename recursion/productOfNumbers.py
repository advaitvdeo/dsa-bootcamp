def productOfNumbers(x, y):
    if not y:
        return 0

    val = x + productOfNumbers(x, y-1)
    return val


x = 10
y = 15
print(productOfNumbers(x, y))

