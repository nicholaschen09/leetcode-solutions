# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
# 
# You must write an algorithm that runs in linear time and uses linear extra space.
#  
# Example 1:
# 
# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
# Example 2:
# 
# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
#  
# Constraints:
# 
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        min_num, max_num = min(nums), max(nums)
        if min_num == max_num:
            return 0  # All numbers are the same, so gap is 0.

        n = len(nums)
        bucket_size = max(1, (max_num - min_num) // (n - 1))  # Minimum bucket size = 1
        bucket_count = (max_num - min_num) // bucket_size + 1  # Total buckets needed

        # Initialize buckets with (min=inf, max=-inf) values
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

        # Place numbers in buckets
        for num in nums:
            idx = (num - min_num) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)  # Update bucket min
            buckets[idx][1] = max(buckets[idx][1], num)  # Update bucket max

        # Compute max gap between successive non-empty buckets
        prev_max = min_num
        max_gap = 0

        for bucket_min, bucket_max in buckets:
            if bucket_min == float('inf'):
                continue  # Skip empty buckets
            max_gap = max(max_gap, bucket_min - prev_max)
            prev_max = bucket_max  # Move to next bucket

        return max_gap
