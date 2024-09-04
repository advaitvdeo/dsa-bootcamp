def display(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]:
                print("K", end=' ')
            else:
                print("X", end=' ')
        print("")


def isValid(board, row, col):
    if row >= 0 and row < len(board) and col >= 0 and col < len(board):
        return True
    return False

def isSafe(board, row, col):
    if isValid(board, row-2, col+1) and board[row-2][col+1]:
        return False
    if isValid(board, row-2, col-1) and board[row-2][col-1]:
        return False
    if isValid(board, row-1, col+2) and board[row-1][col+2]:
        return False
    if isValid(board, row-1, col-2) and board[row-1][col-2]:
        return False
    return True

def nKnights(board, row, col, k):
    if k == 0:
        display(board)
        print("")
        return 1

    count = 0
    if row == len(board)-1 and col == len(board):
        return 0

    if col >= len(board):
        count += nKnights(board, row+1, 0, k)
        return count

    if isSafe(board, row, col):
        board[row][col] = True
        count += nKnights(board, row, col+1, k-1)
        board[row][col] = False

    count += nKnights(board, row, col+1, k)
    return count


board = [[0 for i in range(4)] for j in range(4)]
print(nKnights(board, 0, 0, 4))