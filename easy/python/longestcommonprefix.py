"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: #if nothing return nothing
            return ""
        
        strs.sort() # sort strs in ascending alphabetical order to easily identify common prefix

        prefix = "" # var to hold prefix
        for i in range(min(len(strs[0]), len(strs[-1]))): # loops through the word with the smallest length in strs from beginning to end of list
            if strs[0][i] == strs[-1][i]: # checks each letter in first and last to compare differences
                prefix += strs[0][i]
            
            else:
                break
            
        return prefix