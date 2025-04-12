# Given two binary strings a and b, return their sum as a binary string.
#  
# Example 1:
# 
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
#  
# Constraints:
# 
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1  # pointer for string a
        j = len(b) - 1  # pointer for string b
        carry = 0     # to keep track of the carry over
        result = []   # using a list to collect binary digits
        
        # Loop until both strings are fully traversed and there's no carry left
        while i >= 0 or j >= 0 or carry:
            total = carry  # start with the current carry
            if i >= 0:
                total += int(a[i])  # add digit from a if available
                i -= 1
            if j >= 0:
                total += int(b[j])  # add digit from b if available
                j -= 1
            
            carry = total // 2        # update carry (either 0 or 1)
            result.append(str(total % 2))  # the remainder is the current binary digit
        
        # The digits are in reverse order, so reverse them to get the final result
        return ''.join(reversed(result))
