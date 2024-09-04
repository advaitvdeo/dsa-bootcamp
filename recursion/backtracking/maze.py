def countMazePath(arr, r, c):
    if r == 1 or c == 1:
        return 1

    right = countMazePath(arr, r-1, c)
    down = countMazePath(arr, r, c-1)

    return right + down



def printMazePath(arr, r, c, path):
    if r == 1 and c == 1:
        print(path)
        return

    if r < 1 or c < 1:
        return

    printMazePath(arr, r-1, c, path + 'R')
    printMazePath(arr, r, c-1, path + 'D')



def getMazePath(arr, r, c, path):
    if r == 1 and c == 1:
        return [path]

    if r < 1 or c < 1:
        return []

    left = getMazePath(arr, r-1, c, path + 'R')
    right = getMazePath(arr, r, c-1, path + 'D')

    return left + right


arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(countMazePath(arr, len(arr), len(arr[0])))
printMazePath(arr, len(arr), len(arr[0]), "")
print(getMazePath(arr, len(arr), len(arr[0]), ""))