# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        value = []
        while head:
            value.append(head.val)
            head = head.next
        decimal =0
        n = len(value)

        for i in range(n):
            decimal+=value[i]*(2**(n-1-i))
        print(decimal)
        return decimal

