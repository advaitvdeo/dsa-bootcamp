def firstUpperCase(string):
    if not string:
        return ""

    ch = string[0]
    if ch == ch.upper():
        return ch

    return firstUpperCase(string[1:])


string = "geeksforgeeKs"
print(firstUpperCase(string))