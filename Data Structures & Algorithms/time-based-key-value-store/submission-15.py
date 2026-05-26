### Bruteforce ###
# Given : time is in increasing order only
'''
class TimeMap:

    def __init__(self):
        self.timedict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.timedict:
            self.timedict[key] = []
        self.timedict[key].append((value,timestamp))
        print(self.timedict)

    def get(self, key: str, timestamp: int) -> str:
        
        res = ''
        if key in self.timedict:
            for i in self.timedict[key]:
                if i[1] <= timestamp:
                    res = i[0]
        return res
'''


### Binary Search ###
class TimeMap:

    def __init__(self):
        self.timedict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.timedict:
            self.timedict[key] = []
        self.timedict[key].append((value,timestamp))
        print(self.timedict)

    def get(self, key: str, timestamp: int) -> str:
        
        res = ''
        ### For anything other than normal,modified or lowerbound we use upperbound ###
        # Last occurence or lower, therefore increment l till our value is less than equal to target
        # So l will be on higher position, we want l-1
        # l-1 so we have to be careful because l can be 0 so left bound check
        ### Upperbound ###
        if key in self.timedict:
            nums = self.timedict[key]
            l = 0
            r = len(nums)  ## Excluded since position can be out of bounds

            #Scanning for left to right till l == r
            while l < r :

                m = (l+r)//2

                if nums[m][1] <= timestamp:
                    l = m + 1
                else:
                    r = m

            # Lower bound check if l is 0 then not found 
            res = nums[l-1][0] if l > 0 else ''
            
        return res          





        """
        if key in self.timedict:
 
            ### Upper Bound Standard - pure ###
            # Upper bound gives first greater index
            # Since unique thus only next greater required
            # if nums[l][1] is lower return that or return empty
            nums = self.timedict[key]
            l = 0
            r = len(nums)

            while l < r:
                m = (r+l)//2
                if timestamp < nums[m][1]:
                    r = m
                else:
                    l = m + 1

            if nums[l-1][1] <= timestamp:    
                res = nums[l-1][0]


        return res

        # OR 
                
        '''
            ### Binary search Upper bound non-standard ###
            nums = self.timedict[key]
            l = 0
            r = len(nums)
            
            while l < r:
                
                m = (r+l)//2
                print(l,r,m)
                if timestamp >= nums[m][1]:
                    l = m + 1
                else:
                    r = m

            print(nums[l-1][1], timestamp)
            if nums[l-1][1] <= timestamp:
                print('return')
                return nums[l-1][0]

        return res
        '''
        """

        
