class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        '''
        # n 
        # n
        hashmap = {}

        for i in range(len(nums)):

            if nums[i] in hashmap :
                if abs(hashmap[nums[i]] - i) <= k:
                    return True

            hashmap[nums[i]] = i 
            

        return False 
        '''

        ### Sliding window + set ###
        # Expand -> when len of hashset is less than k 
        # Check -> if alreay there 
        # Shrink 
        [1,2,3]
        hashset = set()

        L = 0 
        for R in range(len(nums)):

            if len(hashset) > k:
                hashset.remove(nums[L])
                L += 1
            
            if nums[R] in hashset:
                return True
            
            hashset.add(nums[R])
        
        return False

