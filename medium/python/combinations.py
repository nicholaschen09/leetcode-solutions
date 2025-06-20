# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# 
# You may return the answer in any order.
#  
# Example 1:
# 
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
# Example 2:
# 
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
#  
# Constraints:
# 
# 1 <= n <= 20
# 1 <= k <= n

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            # check if the combination is of length k and if true add a copy to the res and return
            if len(comb) == k:
                res.append(comb.copy())
                return

            # loop through from start to n + 1
            for i in range(start, n + 1):
                # add each num 
                comb.append(i)
                # backtrack for n + 1 and comb list
                backtrack(i + 1, comb)
                # pop to try next comb
                comb.pop()

        backtrack(1, [])
        return res

