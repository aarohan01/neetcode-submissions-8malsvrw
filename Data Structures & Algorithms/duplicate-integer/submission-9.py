from collections import defaultdict
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

        ### HashMap ###
        ## Loop throught and add to dictionary/default dict and if already present in the hashmap return True
        # Time : O(n)
        # Space : O(n) -> worst case last letter
        
        ### Works ###
        '''
        res = {}

        for i in nums:
            if i in res:
                return True
            else:
                res[i] = 1
                
        return False
        '''

        res = defaultdict(int)
        for i in nums:
            if i in res:
                return True 
            else:
                res[i] += 1
    
        return False
