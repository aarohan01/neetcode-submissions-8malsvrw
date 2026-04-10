class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ### Bruteforce 1 ###
        # For every number count it if count is  len(nums) // 2 return that number instantly
        # Time : O(n^2)
        # Space : O(1)
        '''
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                    if count >= len(nums) // 2:
                        return nums[i]
        '''



        ### Moore's voting algo ###
        count = 0
        res = None 
        for n in nums:
            
            if count == 0:
                count += 1
                res = n
                continue
            
            if n == res:
                count += 1
            else:
                count -= 1
        return res
            








