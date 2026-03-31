from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.leastRecent = None
        print(f'Capacity : {self.capacity} Current:{len(self.cache)}')

    def get(self, key: int) -> int:
        
        value = self.cache.get(key,-1)
        print(f'Key:{key} Value:{value}')
        '''
        if value != -1:
            self.leastRecent = key
            print(f'recent: {self.leastRecent}')
        '''
        if value != -1:
            self.cache.move_to_end(key)
        return value
        

    def put(self, key: int, value: int) -> None:
        
        # Key exists
        if self.cache.get(key,None) is not None:
            self.cache[key] = value
            print(f' case 1 : key : {key} Val:{self.cache[key]}')
        else:
            # Key does not exist
            
            if len(self.cache) >= self.capacity:
                popped = self.cache.popitem(last=False)
                print(f'case 2 key popped : {popped} Current:{len(self.cache)}')
            self.cache[key] = value
            print(f'case 2 key : {key} Val:{self.cache[key]}')
        self.cache.move_to_end(key)

        
