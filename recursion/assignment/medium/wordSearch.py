def isValid(board, row, col):
    if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]):
        return True
    return False


def wordSearch(board, word, visited, r, c):
    if len(word) == 0:
        return True

    if not isValid(board, r, c):
        return False

    down = up = left = right = False
    if board[r][c] == word[0] and not visited[r][c]:
        visited[r][c] = True
        down = wordSearch(board, word[1:], visited, r+1, c)
        up = wordSearch(board, word[1:], visited, r-1, c)
        left =wordSearch(board, word[1:], visited, r, c-1)
        right = wordSearch(board, word[1:], visited, r, c+1)
        visited[r][c] = False

    return down or up or left or right


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"

rows = len(board)
cols = len(board[0])

visited = [[False for col in range(cols)] for row in range(rows)]
found = False

for r in range(rows):
    for c in range(cols):
        if board[r][c] == word[0]:
            if wordSearch(board, word, visited, r, c):
                found = True
                break

if found:
    print(True)
else:
    print(False)