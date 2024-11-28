def checkIncreasing(num, prev):
    if not num:
        return True

    rem = num % 10
    num = num // 10
    if rem >= prev:
        return False
    return checkIncreasing(num, rem)


def increasingDigits(n, num):
    if num > 10**n:
        return

    if checkIncreasing(num, float('inf')):
        print(num)
    increasingDigits(n, num+1)


def increasingDigit2(start, digit, n, ans):
    if not n:
        ans.append(int(digit))
        return

    for i in range(start, 10):
        str1 = digit + str(i)
        increasingDigit2(i+1, str1, n-1, ans)


n = 2
increasingDigits(n, 10**(n-1))
ans = []
increasingDigit2(1, "", n, ans)
print(ans)