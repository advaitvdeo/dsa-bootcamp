def permutations(string, ds):
    if not string:
        print(ds)
        return

    ch = string[0]
    for i in range(len(ds)+1):
        first = ds[0:i]
        last = ds[i:len(ds)]
        permutations(string[1:], first + ch + last)


def permutationList(string, ds):
    if not string:
        return [ds]

    ch = string[0]
    ans = []
    for i in range(len(ds)+1):
        first = ds[0:i]
        last = ds[i:len(ds)]
        ans += permutationList(string[1:], first + ch + last)

    return ans

def permutationCount(string, ds):
    if not string:
        return 1

    ch = string[0]
    count = 0
    for i in range(len(ds)+1):
        first = ds[0:i]
        last = ds[i:len(ds)]
        count += permutationCount(string[1:], first + ch + last)

    return count

string = "abc"
#permutations(string, "")
print(permutationList(string, ""))
print(permutationCount(string, ""))