def removeDuplicates(string):
    if len(string) < 2:
        return string

    # we dont have to run loop and compare all values one by one
    # we just compare one value and use recursion to do remaining comparison
    if string[0] != string[1]:
        return string[0] + removeDuplicates(string[1:])
    return removeDuplicates(string[1:])


string = "aaaaabbbbbb"
string = "geeksforgeeks"
print(removeDuplicates(string))