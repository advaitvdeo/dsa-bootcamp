# iterative brute force approach
def increasingNumbers(n, ans):
    if n == 0:
        return

    start = 10**(n-1)
    end = 10**n

    for i in range(start, end):
        str_num = str(i)
        bad_number = False
        for j in range(len(str_num)-1):
            if int(str_num[j]) >= int(str_num[j+1]):
                bad_number = True
                break
        if not bad_number:
            ans.append(i)


# recursive approach
def incresingNumber_recursive(start, digit, n, ans):
    if n == 0:
        ans.append(digit)
        return

    for i in range(start, 10):
        str1 = digit + str(i)
        incresingNumber_recursive(i+1, str1, n-1, ans)


n = 2
ans = []
increasingNumbers(n, ans)
print(ans)

ans = []
incresingNumber_recursive(1, "", n, ans)
print(ans)