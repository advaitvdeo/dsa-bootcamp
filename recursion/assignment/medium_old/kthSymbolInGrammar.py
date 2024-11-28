def kthSymbol(n, k, string):
    if n <= 1:
        print(string)
        return string[k-1]

    new_str = string
    for i in range(len(string)):
        if string[i] == '0':
            new_str += '1'
        else:
            new_str += '0'

    return kthSymbol(n-1, k, new_str)


print(kthSymbol(4, 3, "0"))
