def firstUpperCase(string):
    if not string:
        return -1

    if string[0] == string[0].upper():
        return string[0]

    return firstUpperCase(string[1:])


string = "geeksforgeeKs"
print(firstUpperCase(string))