def kthSymbol(n, ds):
    if n == 1:
        return ds

    new_ds = ""
    for ch in ds:
        if ch == '0':
            new_ds += "01"
        else:
            new_ds += "10"

    return kthSymbol(n-1, new_ds)


n = 2
k = 2
print(kthSymbol(n, "0")[k-1])