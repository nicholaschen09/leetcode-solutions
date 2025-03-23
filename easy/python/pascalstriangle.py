# Given an integer numRows, return the first numRows of Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# 
# Example 1:
# 
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# 
# Input: numRows = 1
# Output: [[1]]
#  
# Constraints:
# 
# 1 <= numRows <= 30

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #base case
        if numRows == 1:
            return [[1]]

        # Recursive case: Get the previous rows
        result = self.generate(numRows - 1)  # Generate previous rows
        last_row = result[-1]  # Get the last row
        new_row = [1]  # Start the new row with 1
        
        # Build the current row using the previous row
        for i in range(1, len(last_row)):
            new_row.append(last_row[i - 1] + last_row[i])
        
        new_row.append(1)  # End the row with 1
        
        result.append(new_row)  # Add the new row to the result
        return result