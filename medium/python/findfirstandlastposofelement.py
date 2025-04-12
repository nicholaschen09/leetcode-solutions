# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# 
# If target is not found in the array, return [-1, -1].
# 
# You must write an algorithm with O(log n) runtime complexity.
#  
# Example 1:
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# 
# Input: nums = [], target = 0
# Output: [-1,-1]
#  
# Constraints:
# 
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums: List[int], target: int) -> int:
            right, left, = len(nums) - 1, 0
            first = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        first = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            return first

        def last(nums: List[int], target: int) -> int:
            right, left, last = len(nums) - 1, 0, -1
            last = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        last = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            return last

        return [first(nums, target), last(nums, target)]