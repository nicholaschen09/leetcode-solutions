""""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:

-231 <= x <= 231 - 1
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):  # Negative numbers & numbers ending in 0 (except 0) are not palindromes
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10  # Remove last digit from original number
        
        # If the length is even, both halves should be equal.
        # If the length is odd, ignore the middle digit (reversed_half // 10).
        return x == reversed_half or x == reversed_half // 10
