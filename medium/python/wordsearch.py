# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.
#  
# Example 1:
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#  
# Constraints:
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # set vals for row and col for board
        ROWS, COLS = len(board), len(board[0])
        # store all the letters in curr path so dont revisit again
        path = set()

        # have params for row, col, and index value
        def dfs(r, c, i):
            # if reached end of the word it should be good so return true
            if i == len(word):
                return True
        
            # if any of these following cases, return false
            if (r < 0 or c < 0 or r >= ROWS or 
                c >= COLS or word[i] != board[r][c] or (r,c) in path):
                return False

            # add to path so you don't revisit 
            path.add((r, c))

            # try all the different adj positions for next letter in path
            res = (dfs(r + 1, c, i + 1) 
                   or dfs(r - 1, c, i + 1) 
                   or dfs(r, c - 1, i + 1) 
                   or dfs(r, c + 1, i + 1))

            # remove from path so can be used for the next path check for next letter
            path.remove((r, c))
            return res
        
        # run the dfs method through the entire 2D board
        for r in range(ROWS): 
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
            
        return False