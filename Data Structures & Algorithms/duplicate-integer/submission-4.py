class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        ### Bruteforce ###
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i !=j:
                    return True 
        return False