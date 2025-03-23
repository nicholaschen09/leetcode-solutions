# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node): # create func to traverse inorder
            if not node: # base case
                return  
            inorder(node.left) # go thru left subtree
            result.append(node.val) # add val
            inorder(node.right) # go thru right subtree

        inorder(root) # run the inorder func for root of tree input
        return result # return result