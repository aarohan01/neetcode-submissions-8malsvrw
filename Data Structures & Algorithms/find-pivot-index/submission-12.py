class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        '''
        # O(n)
        # O(n)
        prefix = [0]*(len(nums)+1)
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i-1]


        suffix = [0]*(len(nums)+1)
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1] + nums[i+1]
        

        for i in range(len(nums)):
            
            if  prefix[i] == suffix[i]:
                return i
        return -1
        '''

        
        # O(n)
        # O(1)
        left = 0
        total = sum(nums)

        for i in range(len(nums)):

            if left == (total - left - nums[i]):
                return i

            left += nums[i]

        return -1 
        
            
        