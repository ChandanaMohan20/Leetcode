# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        
        #print(temp)
        s = tuple(set(temp))
        st = sorted(s)
        #print(s)
        if not st:
            return None

        ans = ListNode(st[0])
        curr = ans

        for i in st[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return ans







