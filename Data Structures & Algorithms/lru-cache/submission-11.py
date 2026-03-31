### Bruteforce ###
# Use a list to store key,value pair
# every time its accessed pop that pair and append again 
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =  capacity
        self.cache = []

    def get(self, key: int) -> int:
        
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                pair = self.cache.pop(i)
                self.cache.append(pair)
                print(f'Get: {key} - {self.cache}')
                return pair[1]
        return -1

        

    def put(self, key: int, value: int) -> None:
        
        # Case 1 : Key in cache
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                self.cache[i][1] = value
                pair = self.cache.pop(i)
                self.cache.append(pair)
                print(f'Put : {key} - {self.cache}')
                return
         
        # Case 2 : key not in cache 
        if len(self.cache) < self.capacity:
            self.cache.append([key,value])
            print(f'Put  : {key} - {self.cache}')
        else:
            self.cache.remove(self.cache[0])
            self.cache.append([key,value])
            print(f'Put  : {key} - {self.cache}')

        
                
