def reverseString(string):
    if not string:
        return []

    return reverseString(string[1:]) + [string[0]]


string = ["h","e","l","l","o"]
print(reverseString(string))