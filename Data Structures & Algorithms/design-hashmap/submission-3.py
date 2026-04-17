class ListNode:

    # For chaining
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val 
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hashmap = [None]*1000

    def put(self, key: int, value: int) -> None:
        
        bucket = key % 1000
        cur = self.hashmap[bucket]
        while cur:
            if cur.key == key:
                cur.val = value
                return
            cur = cur.next

        node = ListNode(key,value)
        if self.hashmap[bucket] == None:
            self.hashmap[bucket] = node
        else:
            cur = self.hashmap[bucket]
            while cur.next:
                cur = cur.next
            cur.next = node

    def get(self, key: int) -> int:


        bucket = key % 1000
        if self.hashmap[bucket] == None:
            return -1
        
        cur = self.hashmap[bucket]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1


        

    def remove(self, key: int) -> None:

        bucket = key % 1000
        if self.hashmap[bucket] is not None:
            cur = self.hashmap[bucket]
            if cur.key == key:
                self.hashmap[bucket] = cur.next
            else:
                while cur:
                    prev = cur
                    cur = cur.next 
                    if cur.key == key:
                        prev.next = cur.next
                        return
                    
            

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)