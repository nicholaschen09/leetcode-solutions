# Given a string s, remove duplicate letters so that every letter appears once and only once. 
# You must make sure your result is the smallest in lexicographical order among all possible results.
#  
# Example 1:
# 
# Input: s = "bcabc"
# Output: "abc"
# Example 2:
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
#  
# Constraints:
# 
# 1 <= s.length <= 104
# s consists of lowercase English letters.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_pos = {char: i for i, char in enumerate(s)}
        result = []
        seen = set()
        for i, char in enumerate(s):
            if char not in seen:
                while result and char < result[-1] and i < last_pos[result[-1]]: # lexicographical check and if more duplicates in end of string
                    seen.discard(result.pop())
                seen.add(char)
                result.append(char)
        return "".join(result)

