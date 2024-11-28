def removeConsecutiveDuplicate(string):
    if len(string) < 2:
        return string

    if string[0] != string[1]:
        return string[0] + removeConsecutiveDuplicate(string[1:])
    return removeConsecutiveDuplicate(string[1:])


print(removeConsecutiveDuplicate("aaaaabbbbbb"))
