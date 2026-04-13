class ListNode:

    def __init__(self, key, val, next=None, prev=None):
        self.key = key 
        self.val = val 
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):

        self.cache = {}
        self.capacity = capacity 

        self.head, self.tail = ListNode(-1,-1), ListNode(-1,-1)
        self.head.next, self.tail.prev = self.tail, self.head
        

    def insert(self, key: int, val: int) -> int:
        
        # We always insert at the end of linked list
        node = ListNode(key,val)
        prev, next = self.tail.prev, self.tail

        node.prev, node.next = prev, next
        prev.next, next.prev = node, node

        # Insert to dict
        self.cache[key] = node

        print(f'Inserted {key}:{val}')
    
    def remove(self, rkey=None):
        
        # We remove either the rkey or by default the first key after head
        # Store the key to remove before deleting the node
        if rkey == None:
            rkey = self.head.next.key
        
        prev, next = self.cache[rkey].prev, self.cache[rkey].next
        prev.next, next.prev = next, prev

        # Delete from dict
        del self.cache[rkey]

        print(f'Removed {rkey}')


    def get(self, key: int) -> int:

        if key in self.cache:
            val = self.cache[key].val 
            self.remove(key)
            self.insert(key,val)
            return val
        print(f'Key not found {key}')
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(key)
            self.insert(key,value)
        else:
            if len(self.cache) >= self.capacity:
                self.remove()

            self.insert(key,value)
        
