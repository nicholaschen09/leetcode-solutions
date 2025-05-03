# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
# - The left subtree of a node contains only nodes with keys less than the node's key.
# - The right subtree of a node contains only nodes with keys greater than the node's key.
# - Both the left and right subtrees must also be binary search trees.
#
# Example 1:
# Input: root = [2,1,3]
# Output: true
#
# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
# Constraints:
# - The number of nodes in the tree is in the range [1, 10^4].
# - -2^31 <= Node.val <= 2^31 - 1

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # A helper function that performs a depth-first search (DFS) through the tree.
        # It maintains the current allowable range of values (min_val, max_val) for each node.
        def dfs(node, min_val, max_val):
            if not node: 
                return True
            # Validate that the current node's value is within the allowed range.
            if not (min_val < node.val < max_val):
                return False
            # Recursively validate the left subtree and right subtree.
            return (dfs(node.left, min_val, node.val)) and (dfs(node.right, node.val, max_val))
        
        # Start the recursion with initial range (-infinity, infinity) to allow any value at the root.
        return dfs(root, float('-inf'), float('inf'))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # take in node value, max and min value 
        # dfs bc its better to see entire tree rather than levels diff
        def dfs(node, min_val, max_val):
            if not node: 
                return True
            # make sure node value is valid
            if not (min_val < node.val < max_val):
                return False
            # check left and right subtree
            return (dfs(node.left, min_val, node.val)) and (dfs(node.right, node.val, max_val))
        
        # start the recursive loop and make min and max -infinity since no restrictions at root level
        return dfs(root, float('-inf'), float('inf'))