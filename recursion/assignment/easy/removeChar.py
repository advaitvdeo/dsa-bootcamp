def removeChar(string):
    if not string:
        return ""

    ret_str = ""
    if string[0] == 'a':
        upstream = removeChar(string[1:])
    else:
        ret_str = string[0]
        upstream = removeChar(string[1:])
    return ret_str + upstream

string = "baccao"
print(removeChar(string))