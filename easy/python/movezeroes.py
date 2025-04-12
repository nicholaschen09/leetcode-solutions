# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
#  
# Example 1:
# 
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# 
# Input: nums = [0]
# Output: [0]
#  
# Constraints:
# 
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzero_index = 0
         # First pass: move non-zero elements to the beginning of the list
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonzero_index], nums[i] = nums[i], nums[nonzero_index] # swapping adjacent elements in list
                nonzero_index += 1