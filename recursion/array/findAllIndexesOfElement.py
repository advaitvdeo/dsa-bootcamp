# This is an important pattern in recursion where we pass a argument to the function
# this argument holds the final ans
# we return this argument in the base condition

def findAllIndexes(arr, target, index, ans_arr):
    if index == len(arr):
        return ans_arr

    if arr[index] == target:
        ans_arr.append(index)

    return findAllIndexes(arr, target, index+1, ans_arr)


arr = [1, 2, 3, 4, 4, 9]
print(findAllIndexes(arr, 4, 0, []))