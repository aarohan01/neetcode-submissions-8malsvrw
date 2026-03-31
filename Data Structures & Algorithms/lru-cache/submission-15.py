class ListNode:

    def __init__(self, key, val, next=None, prev=None):

        # Doubly linked list storing key-value
        self.key = key
        self.val = val
        self.next, self.prev = next, prev

class LRUCache:

    def __init__(self, capacity: int):
        
        # HashMap and capacity
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes and pointers to track LRU and MRU
        # left.next is LRU, right.prev is MRU

        self.left, self.right  = ListNode(0,0),ListNode(0,0)

        # Empty list left to right and vice versa 
        self.left.next = self.right
        self.right.prev  = self.left

    def remove(self, key: int) -> ListNode:

        '''
        Since cache key value pair stores key and the node as value.
        We can use it as a pointer to directly access node
        '''
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev 
        del self.cache[key]
        return node

    def insert(self, key, node: ListNode) -> None:
        
        '''
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev = node
        node.prev.next = node
        '''
        self.right.prev.next = node
        node.prev = self.right.prev

        node.next = self.right
        self.right.prev = node

        


    def get(self, key: int) -> int:

        if key in self.cache:
            
            node = self.remove(key)
            self.insert(key,node)
            self.cache[key] = node
            print(f'Get {key} - {self.right.prev}')
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        

        # Case 1: key exists
        if key in self.cache:

            # Update and move to end
            node = self.remove(key)
            node.val = value
            self.insert(key,node)
            self.cache[key] = node
        
        else:

            # Case 2 : less than capacity
            # Create a node and insert in list and hashmap
            if len(self.cache) < self.capacity:
                node = ListNode(key,value)
                self.insert(key,node)
                self.cache[key] = node
                
            else:
                lru = self.left.next
                print(lru.key)
                removed = self.remove(lru.key)
                node = ListNode(key,value)
                self.insert(key,node)
                self.cache[key] = node


        print(f'Put {key} - {self.right.prev}')


        
