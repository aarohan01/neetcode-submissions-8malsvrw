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

### Naive Solution ### 
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
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)