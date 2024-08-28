# pattern 1: In this pattern, we are comparing the array elements separately
# depending on the result of comparison, we are calling function
# at the end we are returning False because if condition is true, it would have called the function
def isSorted(arr, index):
    if index == len(arr)-1:
        return True

    if arr[index] <= arr[index+1]:
        return isSorted(arr, index+1)

    return False

# Pattern 2: In this patter, we are comparing array elements and calling the function but joining these 2 conditions
# using AND operator
# this is more of a short cut pattern and we don't have a return statement at the end

def isSorted2(arr, index):
    if index == len(arr) - 1:
        return True

    return arr[index] <= arr[index+1] and isSorted2(arr, index+1)


arr = [1, 2, 4, 5, 71, 8, 10]
#arr = [20, 20, 45, 89, 89, 90]
#arr = [20, 20, 78, 98, 99, 97]
print(isSorted(arr, 0))
print(isSorted2(arr, 0))