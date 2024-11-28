# def countMazePath(arr, r, c):
#     if r == 1 or c == 1:
#         return 1
#
#     right = countMazePath(arr, r-1, c)
#     down = countMazePath(arr, r, c-1)
#
#     return right + down
#
#
#
# def printMazePath(arr, r, c, path):
#     if r == 1 and c == 1:
#         print(path)
#         return
#
#     if r < 1 or c < 1:
#         return
#
#     printMazePath(arr, r-1, c, path + 'R')
#     printMazePath(arr, r, c-1, path + 'D')
#
#
#
# def getMazePath(arr, r, c, path):
#     if r == 1 and c == 1:
#         return [path]
#
#     if r < 1 or c < 1:
#         return []
#
#     left = getMazePath(arr, r-1, c, path + 'R')
#     right = getMazePath(arr, r, c-1, path + 'D')
#
#     return left + right


# number of ways
def maze(arr, r, c):
    if r == len(arr)-1 and c == len(arr[0])-1:
        return 1

    if r >= len(arr) or c >= len(arr[0]):
        return 0

    return maze(arr, r, c+1) + maze(arr, r+1, c)


def maze_path(arr, r, c, ds):
    if r == len(arr)-1 and c == len(arr[0])-1:
        print(ds)
        return

    if r >= len(arr) or c >= len(arr[0]):
        return 0

    maze_path(arr, r, c+1, ds + 'R')
    maze_path(arr, r+1, c, ds + 'D')


def maze_path_list(arr, r, c, ds, ans):
    if r == len(arr)-1 and c == len(arr[0])-1:
        ans.append(ds)
        return

    if r >= len(arr) or c >= len(arr[0]):
        return

    maze_path_list(arr, r, c+1, ds + 'R', ans)
    maze_path_list(arr, r+1, c, ds + 'D', ans)

def maze_path_local(arr, r, c, ds):
    if r == len(arr)-1 and c == len(arr[0])-1:
        return [ds]

    ans = []
    if r >= len(arr) or c >= len(arr[0]):
        return []

    ans += maze_path_local(arr, r+1, c, ds + 'D')
    ans += maze_path_local(arr, r, c+1, ds + 'R')

    return ans

arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(countMazePath(arr, len(arr), len(arr[0])))
# printMazePath(arr, len(arr), len(arr[0]), "")
# print(getMazePath(arr, len(arr), len(arr[0]), ""))

# print(maze(arr, 0, 0))
# maze_path(arr, 0, 0, "")
# ans = []
# maze_path_list(arr, 0, 0, "", ans)
# print(ans)
print(maze_path_local(arr, 0, 0, ""))