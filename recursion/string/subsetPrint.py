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



string = "abc"
#subsetRecursive(string, "")
subsetLoop(string, "", 0)