def oneToN(n, index):
    if index == n:
        print(index)
        return

    print(index)
    oneToN(n, index + 1)


oneToN(10, 1)