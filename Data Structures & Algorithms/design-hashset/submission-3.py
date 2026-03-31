### Bruteforce ###
'''
class MyHashSet:

    def __init__(self):
        self.hash = []
        

    def add(self, key: int) -> None:
        if key not in self.hash:
            self.hash.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash.remove(key)
        

    def contains(self, key: int) -> bool:
        return (key in self.hash)
        
'''

### Solution - Works ### 
# Time : O(1)
# Space : O(n) or O(k)
'''
class MyHashSet:

    def __init__(self):
        
        # Given key will be number between 0 to 1,000,000
        # Bounded range 
        self.data = [False]*1000000

    def add(self, key: int) -> None:
        if not self.data[key]:
            self.data[key] = True 
        

    def remove(self, key: int) -> None:
        if self.data[key]:
            self.data[key] = False 
        

    def contains(self, key: int) -> bool:

        return self.data[key]
'''

### Solution - More optimized ###
# Using bit masking 
# Time : O(n)
# Space : O(k) much smaller k
class MyHashSet:

    def __init__(self):
        
        # Given key will be number between 0 to 1,000,000
        # Bounded range 
        # Assuming 32 bit integer so to represent more than a million number 31251 buckets required
        # 32*31251 > 1 mil
        self.data = [0]*31251 
        # Every int has 32 flag representing 32 keys 

    def add(self, key: int) -> None:

        # Flag to set 
        mask  = key % 32 

        # Bucket 
        bucket = key // 32 
        
        # Set bit 
        self.data[bucket]  |= ( 1 << mask )
        

    def remove(self, key: int) -> None:

        # Flag to set 
        mask  = key % 32 
        
        # Bucket 
        bucket = key // 32 

        # Unset bit 
        self.data[bucket] &= ~(1 << mask)

    def contains(self, key: int) -> bool:

        # Flag to set 
        mask  = key % 32 
        
        # Bucket 
        bucket = key // 32 
        
        # Check set 
        if self.data[bucket] & ( 1 << mask ) != 0:
            return True 
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)