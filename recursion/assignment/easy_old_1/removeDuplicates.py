def removeDuplicates(string, new_string):
    if not string:
        return new_string

    ch = string[0]
    if new_string and new_string[-1] == ch:
        return removeDuplicates(string[1:], new_string)
    else:
        return removeDuplicates(string[1:], new_string + ch)


string = "aabccba"
print(removeDuplicates(string, ""))