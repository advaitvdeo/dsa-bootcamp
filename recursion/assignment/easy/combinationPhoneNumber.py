def helper(arr, index, subset, ans, m):
    if index >= len(arr):
        ans.append(subset[:])
        return

    str = m[arr[index]]
    for i in range(len(str)):
        helper(arr, index+1, subset + str[i], ans, m)


def combinationPhoneNumber(arr):
    ans = []
    m = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    helper(arr, 0, "", ans, m)
    return ans


arr = "23"
print(combinationPhoneNumber(arr))
