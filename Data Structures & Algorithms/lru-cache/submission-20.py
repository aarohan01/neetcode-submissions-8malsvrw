### Bruteforce ###
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

        
        
