def reverseString(string, ans):
    if not string:
        return []

    reverseString(string[1:], ans)
    ans += [string[0]]
    return ans


string = ["h", "e", "l", "l", "o"]
print(reverseString(string, []))