def primeOrNot(num, val):
    if val > num // 2:
        return True

    if num % val == 0:
        return False

    return primeOrNot(num, val + 1)


num = 136
val = 2
if primeOrNot(num, val):
    print("Is Prime")
else:
    print("Not prime")