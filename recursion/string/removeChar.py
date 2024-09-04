def removeChar(s, new_s):
    if not s:
        return new_s

    if s[0] != 'a':
        new_s += s[0]

    return removeChar(s[1:], new_s)



def removeChar2(s):
    if not s:
        return ""

    if s[0] != 'a':
        return s[0] + removeChar2(s[1:])
    return removeChar2(s[1:])

s = "abcdauta"
new_s = ""
print(removeChar(s, new_s))
print(removeChar2(s))