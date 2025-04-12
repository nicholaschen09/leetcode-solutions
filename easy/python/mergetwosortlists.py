# You are given the heads of two sorted linked lists list1 and list2.
# 
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# 
# Return the head of the merged linked list.
#  
# Example 1:
# 
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# 
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
# 
# Input: list1 = [], list2 = [0]
# Output: [0]
#  
# Constraints:
# 
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to convert linked list to Python list and sort
        def sortList(head: ListNode) -> ListNode:
            # Step 1: Convert the linked list to a list
            nums = []
            current = head
            while current:
                nums.append(current.val)
                current = current.next

            # Step 2: Sort the list
            nums.sort()  # Sorts in ascending order

            # Step 3: Convert the sorted list back to a linked list
            dummy = ListNode()
            current = dummy
            for num in nums:
                current.next = ListNode(num)
                current = current.next

            return dummy.next

        # Sort both lists
        list1 = sortList(list1)
        list2 = sortList(list2)

        # Merge the two sorted lists
        dummy = ListNode()
        current = dummy
        
        # Merge process
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If one list is exhausted, append the other list
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next
