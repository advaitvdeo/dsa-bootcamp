def fibo(n):
    if n <= 2:
        return 1

    return fibo(n-1) + fibo(n-2)

n = 8
print(fibo(n))