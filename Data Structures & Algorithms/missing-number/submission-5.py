class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ### Bruteforce ###
        # Time: O(n^2)
        # Space: O(1)
        '''
        for i in range(len(nums)+1):

            if i not in nums:
                return i
        '''

        ### Sorting ###
        # Sort and check diff 
        # Time: O(nlogn)
        # Space: O(1)
        '''
        nums.sort()
        if nums[0] != 0:
            return 0
        if nums[-1] != len(nums):
            return len(nums)

        for i in range(len(nums)-1):

            if nums[i+1]-nums[i] != 1:
                return nums[i]+1
        '''


        ### XOR ###

        res = 0
        for i in range(len(nums)+1):
            res ^= i
        
        for i in range(len(nums)):
            res ^= nums[i]
        return res
        
