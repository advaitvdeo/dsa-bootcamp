def stringLength(string):
    if not string:
        return 0

    return 1 + stringLength(string[1:])

print(stringLength("GEEKSFORGEEKS"))