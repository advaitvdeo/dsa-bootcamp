# l1 + l2 = nums
# l1 - l2 = target
# 2 * l1 = sum(nums) + target
# l1 = (sum(nums) + target) / 2
def targetSum(nums, target, index):
    if target == 0:
        return 1

    if index >= len(nums):
        return 0

    count = 0
    if nums[index] <= target:
        count += targetSum(nums, target - nums[index], index+1)
    count += targetSum(nums, target, index+1)
    return count


nums = [1,1,1,1,1]
target = 3
target = (sum(nums) + target)//2
print(targetSum(nums, target, 0))