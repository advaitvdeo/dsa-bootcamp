def print1toN(n):
    if not n:
        return

    print1toN(n-1)
    print(n)

n = 10
print1toN(n)