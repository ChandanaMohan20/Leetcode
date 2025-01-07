# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = []
        curr = head

        while curr:
            temp.append(curr.val)
            curr = curr.next
        index = len(temp) - n
        
        new_list= temp[:index]+temp[index+1:]
        
        

        
        
        if not new_list:
            return None

        head = ListNode(new_list[0])
        curr= head

        for i in new_list[1:]:
            curr.next= ListNode(i)
            curr = curr.next
        return head



        