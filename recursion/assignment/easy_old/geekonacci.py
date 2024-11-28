def geekonacci(number):
    if number == 1:
        return 1
    if number == 2:
        return 3
    if number == 3:
        return 2

    return geekonacci(number-1) + geekonacci(number-2) + geekonacci(number-3)

print(geekonacci(6))