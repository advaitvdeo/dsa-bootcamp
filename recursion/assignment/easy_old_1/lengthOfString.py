def stringLen(string):
    if not string:
        return 0

    return 1 + stringLen(string[1:])


string = "GEEKSFORGEEKS"
print(stringLen(string))