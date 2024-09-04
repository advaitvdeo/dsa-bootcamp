def sumOfNumbers(n):
    if not n:
        return 0

    return n + sumOfNumbers(n-1)


n = 100
print(sumOfNumbers(n))