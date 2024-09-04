def phonePad(string, ds):
    if not string:
        print(ds)
        return

    digit = int(string[0])
    for i in range((digit-1) * 3, digit * 3):
        if i < 26:
            ch = chr(ord('a') + i)
            phonePad(string[1:], ds+ch)


def phonePadList(string, ds):
    if not string:
        return [ds]

    digit = int(string[0])
    ans = []
    for i in range((digit-1) * 3, digit * 3):
        if i < 26:
            ch = chr(ord('a') + i)
            ans += phonePadList(string[1:], ds+ch)
    return ans


string = "99"
phonePad(string, "")
print(phonePadList(string, ""))