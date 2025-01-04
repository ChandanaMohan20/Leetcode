# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = set()
        
        while head:
            if head in temp:
                return True

            temp.add(head)
            head = head.next
        return False
        
        