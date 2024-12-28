def subseq(string, ds):
    if not string:
        return [ds]

    ans = []
    ans += subseq(string[1:], ds + string[0])
    ans += subseq(string[1:], ds)

    return ans


string = "abc"
print(subseq(string, ""))
