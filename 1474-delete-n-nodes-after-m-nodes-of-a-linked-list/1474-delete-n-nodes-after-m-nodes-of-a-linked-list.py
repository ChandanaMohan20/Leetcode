# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        current = head
        while(current):
            for i in range(0,m-1):
                if current is None:
                    return head
                current = current.next
                
            temp = current
            
            for i in range(0,n+1):
                if temp is None:
                    break
                temp = temp.next
                
            if current:
                
                
                current.next = temp
                current = temp
        return head
           
                
        
            