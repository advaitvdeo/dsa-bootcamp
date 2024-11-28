def sumOfNumbers(n):
    if n == 1:
        return 1

    return n + sumOfNumbers(n-1)

n = 5
print(sumOfNumbers(n))