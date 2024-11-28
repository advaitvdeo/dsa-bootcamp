def oneToN(number):
    if not number:
        return

    oneToN(number-1)
    print(number)


oneToN(9)