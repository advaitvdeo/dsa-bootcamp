def isPalindrom(string):
    return string == string[::-1]

def palindromPartitions(string, index, ds, ans):
    if index == len(string):
        ans.append(ds)
        return

    for i in range(index, len(string)):
        if isPalindrom(string[index:i+1]):
            palindromPartitions(string, i+1, ds + [string[index:i+1]], ans)


string = "nitin"
ans = []
palindromPartitions(string, 0, [], ans)
print(ans)
