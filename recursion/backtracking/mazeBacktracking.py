def printPaths(arr, r, c, path):
    if r == len(arr)-1 and c == len(arr[0])-1:
        print(path)
        return

    if r == len(arr) or c == len(arr[0]):
        return

    if not arr[r][c]:
        return

    arr[r][c] = False

    if r > 0:
        printPaths(arr, r-1, c, path + 'U')

    if c > 0:
        printPaths(arr, r, c-1, path + 'L')

    if c < len(arr[0])-1:
        printPaths(arr, r, c+1, path + 'R')

    if r < len(arr)-1:
        printPaths(arr, r+1, c, path + 'D')

    arr[r][c] = True


def printPathMetrics(arr, r, c, path, mat, step):
    if r == len(arr)-1 and c == len(arr[0])-1:
        mat[r][c] = step
        for i in range(len(mat)):
            print(mat[i])
        print(path)
        return

    if r >= len(arr) or c >= len(arr[0]):
        return

    if not arr[r][c]:
        return

    arr[r][c] = False
    mat[r][c] = step

    if r > 0:
        printPathMetrics(arr, r-1, c, path + 'U', mat, step+1)

    if c > 0:
        printPathMetrics(arr, r, c-1, path + 'L', mat, step+1)

    if c < len(arr[0])-1:
        printPathMetrics(arr, r, c+1, path + 'R',  mat, step+1)

    if r < len(arr)-1:
        printPathMetrics(arr, r+1, c, path + 'D',  mat, step+1)

    arr[r][c] = True
    mat[r][c] = 0


arr = [[True, True, True], [True, True, True], [True, True, True]]
printPaths(arr, 0, 0, "")
print("----------------------------------------------")
printPathMetrics(arr, 0, 0, "", [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 1)

