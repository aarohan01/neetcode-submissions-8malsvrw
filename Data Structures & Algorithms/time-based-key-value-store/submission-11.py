class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((value,timestamp))
        print(self.hashmap)
        

    def get(self, key: str, timestamp: int) -> str:
        
        '''
        res = ''
        if key in self.hashmap:
            for v, t in self.hashmap[key]:
                if t <= timestamp:
                    res = v
        return res
        '''

        ### Lower bound Binary Search ###
        res = ''

        if key in self.hashmap:
            nums = self.hashmap[key]
            l = 0
            r = len(nums)

            while l < r:
                print(l,r)
                m = (l+r)//2

                if nums[m][1] <= timestamp:
                    print(f'{nums[m][1]} >= {timestamp}')
                    l = m + 1
                else:
                    r = m
            
            res = nums[l-1][0] if l-1 >= 0 else ''

        return res


        
