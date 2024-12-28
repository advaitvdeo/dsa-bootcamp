def helper(arr, index, currSum, reqSum, k, alreadyPicked):
    if k == 0:
        return True
    if currSum == reqSum:
        return helper(arr, 0, 0, reqSum, k-1, alreadyPicked)
    if currSum > reqSum:
        return False
    if index >= len(arr):
        return False

    if alreadyPicked[index] == 1:
        return helper(arr, index+1, currSum, reqSum, k, alreadyPicked)
    else:
        # pick
        alreadyPicked[index] = 1
        op1 = helper(arr, index+1, currSum + arr[index], reqSum, k, alreadyPicked)
        alreadyPicked[index] = 0

        # dont pick
        op2 = helper(arr, index+1, currSum, reqSum, k, alreadyPicked)

        return op1 or op2

def equalSumSubset(arr, k):
    if sum(arr) % k != 0:
        return False
    reqSum = sum(arr) // k
    alreadyPicked = [0]*len(arr)
    return helper(arr, 0, 0, reqSum, k, alreadyPicked)


arr = [4, 3, 1, 3, 4, 3, 1, 2]
k = 3
print(equalSumSubset(arr, k))