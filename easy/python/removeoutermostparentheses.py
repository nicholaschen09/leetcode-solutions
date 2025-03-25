# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
#  
# Example 1:
# 
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:
# 
# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:
# 
# Input: s = "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
#  
# Constraints:
# 
# 1 <= s.length <= 105
# s[i] is either '(' or ')'.
# s is a valid parentheses string.

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        count = 0  # Counter to track depth of parentheses

        for c in s:
            if c == '(':
                if count > 0:  # Avoid outermost '('
                    result.append(c)
                count += 1  # Increase depth
            elif c == ')':
                count -= 1  # Decrease depth
                if count > 0:  # Avoid outermost ')'
                    result.append(c)

        return "".join(result)  # Convert list back to string