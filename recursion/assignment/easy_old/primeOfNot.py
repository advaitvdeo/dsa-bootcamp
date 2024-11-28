def primeOrNot(number, num):
    if number // 2 < num:
        return True


    if number % num == 0:
        return False

    return primeOrNot(number, num+1)


print(primeOrNot(96, 2))