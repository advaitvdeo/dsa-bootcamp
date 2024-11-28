def isPalindrom(string):
    return string == string[::-1]

def palindromPartition(string, ans):
    if not string:
        return ""

    for i in range(len(string)):
        substr = string[:i+1]
        if isPalindrom(substr):
            ans.append(substr)
    palindromPartition(string[1:], ans)


ans = []
string = "nitin"
palindromPartition(string, ans)
print(ans)