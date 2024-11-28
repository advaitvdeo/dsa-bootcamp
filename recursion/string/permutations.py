# def permutations(string, ds):
#     if not string:
#         print(ds)
#         return
#
#     ch = string[0]
#     for i in range(len(ds)+1):
#         first = ds[0:i]
#         last = ds[i:len(ds)]
#         permutations(string[1:], first + ch + last)
#
#
# def permutationList(string, ds):
#     if not string:
#         return [ds]
#
#     ch = string[0]
#     ans = []
#     for i in range(len(ds)+1):
#         first = ds[0:i]
#         last = ds[i:len(ds)]
#         ans += permutationList(string[1:], first + ch + last)
#
#     return ans
#
# def permutationCount(string, ds):
#     if not string:
#         return 1
#
#     ch = string[0]
#     count = 0
#     for i in range(len(ds)+1):
#         first = ds[0:i]
#         last = ds[i:len(ds)]
#         count += permutationCount(string[1:], first + ch + last)
#
#     return count


def permutations(p, up):
    if not up:
        print(p)
        return

    ch = up[0]
    for i in range(len(p)+1):
        f = p[:i]
        s = p[i:]
        permutations(f + ch + s, up[1:])

def permutation_arr(p, up, arr):
    if not up:
        arr.append(p)
        return

    ch = up[0]
    for i in range(len(p)+1):
        f = p[:i]
        s = p[i:]
        permutation_arr(f + ch + s, up[1:], arr)


def permutation_arr2(p, up):
    if not up:
        return [p]

    ch = up[0]
    arr = []
    for i in range(len(p)+1):
        f = p[:i]
        s = p[i:]
        arr += permutation_arr2(f + ch + s, up[1:])
    return arr


string = "abc"
arr = []
permutations("", string)
permutation_arr("", string, arr)
print(permutation_arr2("", string))
print(arr)
# print(permutationList(string, ""))
# print(permutationCount(string, ""))