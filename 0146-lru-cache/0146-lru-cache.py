class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        
        node = self.node_map[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node_to_remove = self.node_map[key]
            self.remove(node_to_remove)
        #adding key to cache
        node = ListNode(key,value)
        
        self.node_map[key] = node
        self.add(node)
        
        if len(self.node_map)> self.capacity :
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            
            del self.node_map[node_to_delete.key]
            
            
        
    def add(self,node):
        prev_node= self.tail.prev
        
        node.prev = prev_node
        prev_node.next = node
        node.next = self.tail
        self.tail.prev = node
        
    def remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)