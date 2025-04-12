# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# 
# There is only one repeated number in nums, return this repeated number.
# 
# You must solve the problem without modifying the array nums and using only constant extra space.
#  
# Example 1:
# 
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
# 
# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:
# 
# Input: nums = [3,3,3,3,3]
# Output: 3
#  
# Constraints:
# 
# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Step 1: Detect the cycle using slow and fast pointers
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]        # Move slow by 1 step
            fast = nums[nums[fast]]  # Move fast by 2 steps
        
        # Step 2: Find the duplicate (cycle entrance)
        slow = 0  # Reset slow to the start
        while slow != fast:
            slow = nums[slow]  # Move 1 step at a time
            fast = nums[fast]
        
        return slow  # The duplicate number