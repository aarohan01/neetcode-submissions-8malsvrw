class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        ### Bruteforce ###
        # Time: o(n)
        # Space: O(n)
        
        hashmap = {}
        res = []
        for n in nums:
            hashmap[n] = hashmap.get(n,0)+1

        
        for key, val in hashmap.items():
            if val == 1:
                res.append(key)
        
        return res
    