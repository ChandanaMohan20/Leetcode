# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next # so that we dont loose the rest of the list
            #reversing directions
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        



