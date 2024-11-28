def kthBit(string, n, k):
    if n == 0:
        return string[k-1]

    str_rev = ""
    for i in range(len(string)):
        if string[i] == '0':
            str_rev += '1'
        else:
            str_rev += '0'
    new_str = string + '1' + str_rev[::-1]

    return kthBit(new_str, n-1, k)


k = 11
n = 4
print(kthBit('0', n-1, k))