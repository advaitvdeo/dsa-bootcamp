def isValid(board, row, col):
    if row >= 0 and col >= 0 and row < len(board) and col < len(board[0]):
        return True
    return False

def wordSearch(board, word, row, col, visited):
    if not word:
        return True

    if not isValid(board, row, col):
        return False

    if visited[row][col]:
        return False

    if board[row][col] != word[0]:
        return False

    visited[row][col] = True
    # go up
    up = wordSearch(board, word[1:], row-1, col, visited)
    # go down
    down = wordSearch(board, word[1:], row+1, col, visited)
    # go left
    left = wordSearch(board, word[1:], row, col-1, visited)
    # go right
    right = wordSearch(board, word[1:], row, col+1, visited)
    visited[row][col] = False

    return up or down or left or right


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"

# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]
# word = "ABCB"

rows = len(board)
cols = len(board[0])
visited = [[False for i in range(cols)] for j in range(rows)]
row = 0
col = 0

found = False
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == word[0]:
            row = r
            col = c
            if wordSearch(board, word, row, col, visited):
                print(True)
                found = True
                break
if not found:
    print(False)