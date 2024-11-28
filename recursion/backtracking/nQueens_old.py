def display(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]:
                print("Q", end=' ')
            else:
                print("X", end=' ')
        print("")


def isSafe(board, row, col):
    # vertical
    for i in range(row):
        if board[i][col]:
            return False

    # diagonal left
    maxLeft = min(row, col)
    for i in range(1, maxLeft+1):
        if board[row-i][col-i]:
            return False

    # diagonal right
    maxRight = min(row, len(board)-col-1)
    for i in range(1, maxRight+1):
        if board[row-i][col+i]:
            return False

    return True



def nQueens(board, row):
    if row == len(board):
        display(board)
        print("\n")
        return 1

    count = 0
    # we place the queen at every row and column
    # rows can be traversed using recursion and column can be traversed using loop

    for col in range(len(board[0])):
        if isSafe(board, row, col):
            board[row][col] = True
            count += nQueens(board, row+1)
            board[row][col] = False  # backtracking

    return count


board = [[0 for i in range(4)] for j in range(4)]
print(nQueens(board, 0))