# Alice and Bob are playing a game. Initially, Alice has a string word = "a".
# 
# You are given a positive integer k.
# 
# Now Bob will ask Alice to perform the following operation forever:
# 
# Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
# For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
# 
# Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.
# 
# Note that the character 'z' can be changed to 'a' in the operation.
#  
# Example 1:
# 
# Input: k = 5
# Output: "b"
# Explanation:
# Initially, word = "a". We need to do the operation three times:
# Generated string is "b", word becomes "ab".
# Generated string is "bc", word becomes "abbc".
# Generated string is "bccd", word becomes "abbcbccd".
# Example 2:
# 
# Input: k = 10
# Output: "c"
#  
# Constraints:
# 
# 1 <= k <= 500

class Solution:
    def kthCharacterHelper(self, k: int, word: str) -> str:
        # Base case: If the current string is long enough, return the k-th character
        if len(word) >= k:
            return word[k - 1]  # 0-based indexing

        # Generate the next part of the string
        next_word = ''.join(chr(ord(c) + 1) if c != 'z' else 'a' for c in word)

        # Recursive call to continue building the string
        return self.kthCharacterHelper(k, word + next_word)

    def kthCharacter(self, k: int) -> str:
        return self.kthCharacterHelper(k, "a")  # Start with initial word "a"