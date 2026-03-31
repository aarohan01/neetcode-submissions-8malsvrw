class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        ### BruteForce ###
        # Loop through 
        '''
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return True
        return False
        '''
        ### Solution 1 ### 
        nums_set = set(nums)
        if len(nums_set) < len(nums):
            return True
        return False