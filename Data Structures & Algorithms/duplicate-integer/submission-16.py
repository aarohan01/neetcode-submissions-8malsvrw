class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        ### Bruteforce ###
        # Time: O(n^2)
        # Space: O(1)
        '''
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i !=j:
                    return True 
        return False
        '''

        ### Set Length ###
        # Time : O(n) -> O(n) + O(1) + O(1) :  create set + set lenght + array length
        # Space : O(n)
        '''
        res =  set(nums)
        if len(res) == len(nums):
            return False 
        return True
        '''


        ### HashSet ### Optimal on average ###
        ## Loop throught and add to set and if already present in the hashset return True
        # Time : O(n)
        # Space : O(n) -> worst case last letter

        res = set()
        for i in nums:
            if i in res:
                return True
            else:
                res.add(i)
        return False
        






