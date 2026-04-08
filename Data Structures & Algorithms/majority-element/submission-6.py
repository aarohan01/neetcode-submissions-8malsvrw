class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ### Bruteforce 1 ###

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                    if count >= len(nums) // 2:
                        return nums[i]
        

            
        '''
        hashmap = {}
        maxfreq = 0
        maxfreqnum = None
        for i in nums:

            hashmap[i] =  hashmap.get(i,0) + 1
            if hashmap[i] > maxfreq:
                maxfreq = hashmap[i]
                maxfreqnum = i

        return maxfreqnum
        '''