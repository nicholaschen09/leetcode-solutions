# Given an integer array nums of unique elements, return all possible subsets (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in any order.
#  
# Example 1:
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
# 
# Input: nums = [0]
# Output: [[],[0]]
#  
# Constraints:
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums) + 1):  # The power set includes subsets of all sizes (from 0 to len(nums))
            result.extend(itertools.combinations(nums, i))  # Get all subsets of size i
        return [list(subset) for subset in result]  # Convert each subset from tuple to list
