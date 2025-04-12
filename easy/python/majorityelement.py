# Given an array nums of size n, return the majority element.
# 
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#  
# Example 1:
# 
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# 
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#  
# Constraints:
# 
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, 0

        for num in nums: # loop through the list
            if count == 0: # check if count is 0 meaning no majority element
                candidate = num # set current num to majority
            if num == candidate: # if the num equal to majority add count
                count += 1 
            else:
                count -= 1 # else minus 1 to get closer to neutral
        
        return candidate