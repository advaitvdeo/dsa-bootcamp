def printStar(r, c):
    if r == 0:
        return

    if c < r:
        print("*", end=' ')
        printStar(r, c+1)
    else:
        print("", end='\n')
        printStar(r-1, 0)


printStar(4, 0)