class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

       
        ### Bruteforce ###
        # Time: O(n^2)
        # Space: O(1)
        '''
        for i in range(len(nums)):
            flag = False
            for j in range(len(nums)):
                
                if i != j and nums[i] == nums[j]:
                    flag = True
                    break
            if not flag:
                return nums[i]
        '''

        ### Hashmap frequency ###
        # Time: O(n)
        # Space: O(n)
        '''
        hashmap = {}
        for i in range(len(nums)):
            
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1


        for val, freq in hashmap.items():

            if freq == 1:
                return val
        '''


        ### Sort and check ###
        # Time: O(nlogn)
        # Space: O(1)
        '''
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        else:
            i = 0
            while i < len(nums):
                
                if i + 1 < len(nums) and nums[i] != nums[i+1]:
                    return nums[i]
                else:
                    i += 2

            return nums[-1]
        '''
        #OR
        '''
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]

        return nums[-1]
        '''
        
        ### XOR - Optimized ###
        # Time: O(n)
        # Space: O(1)
        res = 0
        for num in nums:
            res ^= num
        return res


