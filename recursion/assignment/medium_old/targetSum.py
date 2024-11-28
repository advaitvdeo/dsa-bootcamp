# sum = sum(nums)
# dividing the array into 2 parts - one with +ve integers and one with -ve integers, lets call it s1 and s2
# s1 - s2 = target
# s1 + s2 = sum(nums)
# adding both equations above
# 2*s1 = sum(nums) + target
# s2 = (sum(nums) + target)/2

def targetSum(nums, target, index):
    if target == 0:
        return 1

    if index >= len(nums):
        return 0

    count = 0
    for i in range(index, len(nums)):
        if nums[i] <= target:
            count += targetSum(nums, target - nums[i], i+1)

    return count


nums = [1, 1, 1, 1, 1]
target = 3

print(targetSum(nums, (sum(nums) + target)//2, 0))
