def reverseDigits(num, ans):
    if not num:
        return ans

    rem = num % 10
    ans = ans * 10 + rem
    return reverseDigits(num // 10, ans)

num = 1234
print(reverseDigits(num, 0))