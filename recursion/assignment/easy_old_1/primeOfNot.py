def primeOrNot(num, d):
    if d > num // 2:
        return True

    if num % d == 0:
        return False

    return primeOrNot(num, d+1)


num = 11
print(primeOrNot(num, 2))