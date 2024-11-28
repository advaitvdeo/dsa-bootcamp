import copy
from copy import deepcopy
def subsetRecursive(string, ds):
    if not string:
        print(ds)
        return

    subsetRecursive(string[1:], ds + string[0])
    subsetRecursive(string[1:], ds)


def subsetLoop(string, ds, index):
    if index >= len(string):
        print(ds)
        return

    subsetLoop(string, ds + string[index], index + 1)
    while index + 1 < len(string) and string[index] == string[index+1]:
        index += 1
    subsetLoop(string, ds, index+1)

def subset2(string, ds, ans):
    if not string:
        ans.append(ds)
        return

    # pick
    subset2(string[1:], ds + string[0], ans)
    # not pick
    subset2(string[1:], ds, ans)

def subset_iteration(arr):
    outer = [[]]
    for num in arr:
        for i in range(len(outer)):
            inner = deepcopy(outer[i])
            inner.append(num)
            outer.append(inner)
    return outer


def subset_duplicates(arr):
    outer = [[]]
    for i in range(len(arr)):
        start = 0
        if i > 0 and arr[i] == arr[i-1]:
            start = end + 1
        end = len(outer) - 1
        for j in range(start, len(outer)):
            inner = copy.deepcopy(outer[j])
            inner.append(arr[i])
            outer.append(inner)
    return outer

string = "abc"
#subsetRecursive(string, "")
#subsetLoop(string, "", 0)
# ans = []
# subset2(string, "", ans)
# print(ans)
# arr = [1, 2, 3]
# subsets = subset_iteration(arr)
# for subset in subsets:
#     print(subset, end = " ")

arr = [1, 2, 2]
subsets = subset_duplicates(arr)
for subset in subsets:
    print(subset, end = " ")