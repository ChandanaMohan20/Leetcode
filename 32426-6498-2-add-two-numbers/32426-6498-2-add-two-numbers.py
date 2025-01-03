# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        dummy = ListNode()  # Dummy node to simplify result list creation
        current = dummy  # Pointer to construct the result list
        carry = 0  # Carry for digit addition

        while l1 or l2 or carry:
            # Get the values of the current nodes or 0 if null
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Create a new node with the digit and move the pointer
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes in l1 and l2, if available
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next  # Skip the dummy node and return the result
