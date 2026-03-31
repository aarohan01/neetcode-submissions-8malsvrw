class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ### Bruteforce ###
        # For every element check max consecutive length 
        # If hashset not used and directly checking the list, time complexity will be O(n^3)
        # Time : O(n^2)
        # Space : O(n)
        '''
        hashset = set(nums)
        maxlen = 0
        
        for i in range(len(nums)):
            curlen = 0
            cur = nums[i]
            while cur in hashset:
                curlen += 1
                cur += 1
            maxlen = max(maxlen,curlen)

        print(maxlen)
        return maxlen
        '''

        ### Sorting ###
        if len(nums) <= 1:
            return len(nums)

        nums.sort()
        maxlen = 1
        curlen = 1
        for i in range(1,len(nums)):
            
            if abs(nums[i-1] - nums[i]) == 1:
                curlen += 1
            elif nums[i-1] == nums[i]:
                continue
            else:
                curlen = 1
            maxlen =  max(curlen,maxlen)
        print(maxlen)
        return maxlen
                

        