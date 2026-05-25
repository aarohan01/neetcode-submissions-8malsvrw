class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((value,timestamp))
        print(self.hashmap)
        

    def get(self, key: str, timestamp: int) -> str:
        
        res = ''
        if key in self.hashmap:
            for v, t in self.hashmap[key]:
                if t <= timestamp:
                    res = v
        return res
            
        
