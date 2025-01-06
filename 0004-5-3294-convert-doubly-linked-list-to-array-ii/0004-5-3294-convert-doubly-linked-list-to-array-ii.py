"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:

        while node.prev:
            node = node.prev

        res = []

        while node:
            res.append(node.val)
            node = node.next
        return res

        