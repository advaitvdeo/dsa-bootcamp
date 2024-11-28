def product(num1, num2):
    if num1 == 1:
        return num2

    return num2 + product(num1-1, num2)

num1 = 100
num2 = 5
print(product(num1, num2))