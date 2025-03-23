"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 
Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        right = len(height) - 1 # set the right pointer to the end of the list
        left = 0 # set left ptr to start of list
        area = 0

        while left < right: # while loop
            l = right - left # find the length
            h = min(height[right], height[left]) # find height
            area = max(area, h * l) #compare the current area to the prev area and find max
        
            if height[left] < height[right]: 
                left += 1
            else:
                right -= 1 
      
        return area