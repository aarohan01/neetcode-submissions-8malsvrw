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
        # Time : O(nlogn)
        # Space : O(1) or O(n)
        '''
        # Edge cases
        if len(nums) <= 1:
            return len(nums)

        # Sort 
        nums.sort()

        # For every number starting second element if the previous number 
        # was less than it increment curlen and finally update the maxlen 
        # if same number then skip if diff not 1 then reset curlen
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
        '''


        ### Hashset plus not checking hashset for every number ###
        # Start of sequence is only when than number - 1 is not present 


        hashset = set(nums)
        maxlen = 0
        
        for i in hashset:
            curlen = 0
            if i-1 not in hashset:
                curlen += 1
                while i + 1 in hashset:
                    curlen += 1
                    i += 1
            maxlen = max(curlen,maxlen)        
        return maxlen

        