# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#  
# Example 1:
# 
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
# 
# Input: strs = [""]
# Output: [[""]]
# 
# Example 3:
# 
# Input: strs = ["a"]
# Output: [["a"]]
#  
# Constraints:
# 
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26 # array of alphabet
            for c in s:
                count[ord(c) - ord('a')] += 1 # finds the ascii value for the index of count and adds 1 to count
     
            key = tuple(count) # turns count into tuple to use dictionary
            anagrams[key].append(s) # checks if key is there and adds the word

        return list(anagrams.values()) # returns all the values in anagrams as a list
