def displayBoard(board):
    for row in board:
        for col in row:
            if col:
                print("K ", end=" ")
            else:
                print("X ", end=" ")
        print(" ", end = "\n")

def isValid(board, row, col):
    if row >= 0 and row < len(board) and col >= 0 and col < len(board):
        return True
    return False

def isSafe(board, row, col):
    if isValid(board, row - 2, col - 1):
        if board[row-2][col-1]:
            return False

    if isValid(board, row - 2, col + 1):
        if board[row-2][col+1]:
            return False

    if isValid(board, row - 1, col - 2):
        if board[row-1][col-2]:
            return False

    if isValid(board, row - 1, col + 2):
        if board[row-1][col+2]:
            return False

    return True

def NKnights(board, row, col, knights):
    if knights == 0:
        displayBoard(board)
        print("\n")
        return 1

    count = 0

    if row == len(board)-1 and col == len(board):
        return 0

    if col == len(board):
        count += NKnights(board, row + 1, 0, knights)
        return count

    if isSafe(board, row, col):
        board[row][col] = True
        count += NKnights(board, row, col+1, knights - 1)
        board[row][col] = False

    count += NKnights(board, row, col + 1, knights)
    return count


board = [[0 for i in range(4)] for j in range(4)]
print(NKnights(board, 0, 0, 4))