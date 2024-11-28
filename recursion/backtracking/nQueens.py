def isSafe(board, row, col):
    # going above
    for r in range(row):
        if board[r][col]:
            return False

    # going diag left
    maxLeft = min(row, col)
    for i in range(1, maxLeft+1):
        if board[row-i][col-i]:
            return False

    # going diag right
    maxRight = min(row, len(board)-col-1)
    for i in range(1, maxRight+1):
        if board[row-i][col+i]:
            return False
    return True


def displayBoard(board):
    for row in board:
        for col in row:
            if col:
                print("Q ", end = "")
            else:
                print("X ", end = "")
        print(" ", end = "\n")


def NQueens(board, row):
    if row == len(board):
        displayBoard(board)
        print("\n")
        return 1

    count = 0
    for col in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = True
            count += NQueens(board, row+1)
            board[row][col] = False

    return count


board = [[0 for i in range(4)] for j in range(4)]
print(NQueens(board, 0))