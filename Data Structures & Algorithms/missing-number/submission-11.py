class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ### 
        # nlogn
        # 1
        '''
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
        '''

        ### bitwise xor
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
            res ^= i
        
        res ^= len(nums)
        return res

