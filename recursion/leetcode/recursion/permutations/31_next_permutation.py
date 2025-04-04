# https://leetcode.com/problems/next-permutation/description/
"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory
"""

class Solution:
    def nextPermutation(self, nums):
        # find out index which is smaller when starting from end
        index = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i-1
                break

        if index != -1:
            # calculate swap index, by checking value which is larger then above index value
            swap_index = index
            for i in range(len(nums)-1, index, -1):
                if nums[i] > nums[index]:
                    swap_index = i
                    break

            # swap index and swap_index
            nums[index], nums[swap_index] = nums[swap_index], nums[index]

            # reverse the array from index onwards
        nums[index+1:] = nums[index+1:][::-1]
        return nums

a = Solution()
nums = [2, 3, 1]
print(a.nextPermutation(nums))