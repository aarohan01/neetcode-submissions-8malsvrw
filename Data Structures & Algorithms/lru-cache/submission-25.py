### Bruteforce ###
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        
        for i,k in enumerate(self.cache):
            if k[0] == key:
                n = self.cache.pop(i)
                self.cache.append(k)
                return k[1]
        return -1

    def put(self, key: int, value: int) -> None:
        
        for i,k in enumerate(self.cache):
            if k[0] == key:
                print(self.cache[i])
                self.cache.pop(i)
                self.cache.append((key,value))
                return
        
        if len(self.cache) >= self.capacity:
            self.cache.pop(0)
        self.cache.append((key,value))
        


### Bruteforce ###
'''
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            print(self.cache)
            if len(self.cache) >= self.capacity:
                x = self.cache.popitem(last=False)
                print(f'rem:{x}')

            self.cache[key] = value
'''
        
        
