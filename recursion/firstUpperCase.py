def firstUpperCase(string, index):
    if index == len(string):
        return ""

    # if ord(string[index]) >= 65 and ord(string[index]) <= 90:
    #     return string[index]

    if string[index].isupper():
        return string[index]

    return firstUpperCase(string, index+1)


string = "aDvaIt"
ans = firstUpperCase(string, 0)
print(ans)