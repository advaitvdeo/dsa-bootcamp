def invert(ds):
    new_ds = ""
    for ch in ds:
        if ch == "0":
            new_ds += "1"
        else:
            new_ds += "0"
    return new_ds

def reverse(ds):
    return ds[::-1]


def kthBit(n, ds):
    if n == 1:
        return ds

    new_ds = ds + "1" + reverse(invert(ds))
    return kthBit(n-1, new_ds)


n = 4
k = 11
print(kthBit(n, "0")[k-1])