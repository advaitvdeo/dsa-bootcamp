# using recursion
def substring(string, ans):
    if not string:
        return ""

    for i in range(len(string)):
        ans.append(string[:i+1])

    substring(string[1:], ans)


def substring_iterative(string):
    ans = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            ans.append(string[i:j+1])
    return ans


ans = []
string = "abcd"
substring(string, ans)
print(ans)
print(substring_iterative(string))