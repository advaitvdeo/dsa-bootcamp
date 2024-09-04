import math


def display(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print(" ")


def isSafe(board, row, col, number):
    # check the row
    for i in range(len(board)):
        if board[row][i] == number:
            return False

    # check the col
    for rows in board:
        if rows[col] == number:
            return False

    # check the small boxes
    sqrt = int(math.sqrt(len(board)))
    rowStart = row - row % sqrt
    colStart = col - col % sqrt
    for i in range(rowStart, rowStart + sqrt):
        for j in range(colStart, colStart + sqrt):
            if board[i][j] == number:
                return False

    return True

def sudoku(board):
    n = len(board)
    row = col = -1

    # base condition
    # we are checking if entire sudoku is solved or we are seeing any empty elements
    emptyFound = False
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                row = i
                col = j
                emptyFound = True
                break
        if emptyFound:
            break

    if not emptyFound:
        return True

    # actual logic of recursion and backtracking
    for number in range(1, 10):
        if isSafe(board, row, col, number):
            board[row][col] = number
            if sudoku(board):
                return True
            else:
                board[row][col] = 0

    return False


board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

sudoku(board)
display(board)