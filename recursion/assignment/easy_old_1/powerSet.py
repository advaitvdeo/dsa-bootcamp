def powerSet(string, index, curr):
    if index == len(string):
        return

    if len(curr) > 0:
        print(curr)

    for i in range(index+1, len(string)):
        curr += string[i]
        powerSet(string, i, curr)
        curr = curr[:len(curr)-1]


string = "abc"
powerSet(string, -1, "")