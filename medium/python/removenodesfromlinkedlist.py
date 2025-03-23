"""
You are given the head of a linked list.
Remove every node which has a node with a greater value anywhere to the right side of it.
Return the head of the modified linked list.

Example 1:

Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 
Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        
        # Traverse the list from left to right
        while current:
            # Keep track of the maximum value seen so far
            while stack and stack[-1].val < current.val:
                stack.pop()  # Remove nodes with smaller values
            stack.append(current)  # Add the current node to the stack
            current = current.next
        
        # Rebuild the linked list from the stack
        dummy = ListNode(0)
        current = dummy
        for node in stack:
            current.next = node
            current = current.next
        
        current.next = None  # Ensure the last node's next is None
        return dummy.next  # Return the head of the modified list