def reverseNumber(num):
    if num == 0:
        return 0

    return (num % 10) * 10**(len(str(num))-1) + reverseNumber(num//10)


num = 1234
print(reverseNumber(num))