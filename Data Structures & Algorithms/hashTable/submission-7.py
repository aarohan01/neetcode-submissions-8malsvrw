class ListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        
        ## Dynamic array with capacity 1000 ##
        print("Creating Hashtable")
        self.capacity = capacity
        self.data = [None]*self.capacity
        self.size = 0


    def getBucket(self, key:int) -> int:

        return key % self.capacity

    
    def insert(self, key: int, value: int) -> None:
        
        ## Insert 
        bucket = self.getBucket(key)
        node = ListNode((key,value))
        
        
        if not self.data[bucket]:
            # Case 1 : Empty
            print(f'Insert at empty')
            self.data[bucket] = node 
            self.size += 1

        elif self.data[bucket]:
            
            # Case 2 : Found
            cur = self.data[bucket]
            prev = None
            while cur:
                if cur.val[0] == key:
                    print(f'Found key: {key}')
                    cur.val = (key,value)
                    print(f'key: {cur.val[0]} - val:{cur.val[1]}\n')
                    break
                prev, cur = cur, cur.next

            # Case 3 : Append
            if not cur:
                print(f'Insert appended')
                self.size += 1
                prev.next = node


        print(f"After insert : {self.data}\n")

        ## Resize 
        if self.size / self.capacity >= 0.5:
            self.resize()



    def get(self, key: int) -> int:
        bucket = self.getBucket(key)

        if self.data[bucket]:
            cur = self.data[bucket]
            while cur:
                if cur.val[0] == key:
                    print(f'Get {key} - value {cur.val[1]}\n')
                    return cur.val[1]
                cur = cur.next
        
        return -1



    def remove(self, key: int) -> bool:
        
        bucket = self.getBucket(key)

        # Case 1 : Empty 
        if not self.data[bucket]:
            return False
        
        
        cur = self.data[bucket] 
        prev = None
            
        while cur:
            if cur.val[0] == key:
                
                # Case 2.1 - Found but only one elemnt 
                if not prev and not cur.next :
                    self.data[bucket] = None
                # Case 2.2 - Found at first element but chained
                elif not prev:
                    self.data[bucket] = cur.next
                # Case 2.3 - Found in the chain
                else:
                    prev.next = cur.next

                self.size -= 1
                return True
            prev, cur = cur, cur.next
            
        return False


    def getSize(self) -> int:
        return self.size 


    def getCapacity(self) -> int:
        print(f"capaicy {self.capacity}")
        return self.capacity

    def resize(self) -> None:
        
        self.capacity = self.capacity*2
        self.size = 0
        tmp = self.data 
        self.data = [None]*self.capacity
        
        ## Re-Hashing 
        for i in tmp:
            if i:
                cur = i
                while cur:
                    self.insert(cur.val[0], cur.val[1])
                    cur = cur.next

                




