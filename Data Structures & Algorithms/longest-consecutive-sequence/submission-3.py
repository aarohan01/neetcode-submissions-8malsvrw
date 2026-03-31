class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ### Bruteforce ###
        # For every element check max consecutive length 
        # Time : O(n^2)
        # Space : O(n)
        
        hashset = set(nums)
        maxlen = 0
        
        for i in range(len(nums)):
            curlen = 0
            cur = nums[i]
            while cur in nums:
                curlen += 1
                cur += 1
            maxlen = max(maxlen,curlen)

        print(maxlen)
        return maxlen
        

        ### Sorting ###
                

        