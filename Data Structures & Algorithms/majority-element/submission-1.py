class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ### Bruteforce ###
        
        hashmap = {}
        maxfreq = 0
        maxfreqnum = None
        for i in nums:

            hashmap[i] =  hashmap.get(i,0) + 1
            if hashmap[i] > maxfreq:
                maxfreq = hashmap[i]
                maxfreqnum = i

        return maxfreqnum