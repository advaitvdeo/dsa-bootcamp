def compare(string, used):
    new_used = [0]*26
    for ch in string:
        if new_used[ord(ch) - ord('a')]:
            return False
        new_used[ord(ch)-ord('a')] = 1

    for ch in string:
        if used[ord(ch) - ord('a')]:
            return False

    return True

def helper(arr, index, used, ans):

    if index >= len(arr):
        return ans

    string = arr[index]

    # check current string
    if not compare(string, used):
        return helper(arr, index+1, used, ans)
    else:
        # pick
        for ch in string:
            used[ord(ch) - ord('a')] = 1
        op1 = helper(arr, index+1, used, ans + len(string))
        for ch in string:
            used[ord(ch) - ord('a')] = 0
        # not pick
        op2 = helper(arr, index+1, used, ans)

        return max(op1, op2)

def maxConcatinatedString(arr):
    ans = 0
    used = [0]*26
    return helper(arr, 0, used, ans)


arr = ['cha', 'racf', 'tersasas']
print(maxConcatinatedString(arr))