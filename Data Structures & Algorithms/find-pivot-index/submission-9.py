class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        '''
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

        right = 0
        total = sum(nums)

        for i in range(len(nums)):

            if right == (total - right - nums[i]):
                return i

            right += nums[i]

        return -1 
            
        