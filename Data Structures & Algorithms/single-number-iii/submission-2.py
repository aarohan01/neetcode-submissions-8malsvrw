class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        ### Bruteforce ###
        # Time: o(n)
        # Space: O(n)
        '''
        hashmap = {}
        res = []
        for n in nums:
            hashmap[n] = hashmap.get(n,0)+1

        
        for key, val in hashmap.items():
            if val == 1:
                res.append(key)
        
        return res
        '''


        ### Grouped XOR ###

        xor = 0
        for n in nums:
            xor ^= n
        
        print(xor)


        # Only 1 bit is required to distinguish between 2 groups, lets check the index of last 1 in xor
        idx = None
        for i in range(32):
            if xor & (1 << i) != 0:
                idx = i 
                break
        print(idx)

        ### Split into groups based on the idx has 1
        one, two = 0, 0
        for n in nums:
            
            if n & (1 << idx) != 0:
                one ^= n 
            else:
                two ^= n
        
        return [one,two]
        
            


