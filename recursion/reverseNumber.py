import math
def reverseNumber(num, arg):
    if num % 10 == num:
        return num

    return (num % 10) * (10**arg) + reverseNumber(num//10, arg-1)

num = 1842
print(reverseNumber(num, int(math.log10(num))))
