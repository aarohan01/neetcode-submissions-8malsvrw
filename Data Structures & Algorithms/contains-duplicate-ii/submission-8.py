class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        ### Bruteforce ###
        for L in range(len(nums)):
            for R in range(L+1, min(len(nums), L+k+1)):

                if nums[L] == nums[R]:
                    return True
        return False

        ### HashSet and Sliding window ###
        # Shrink and Check, Expand  
        '''
        hashset = set() # Cur window of size <= k
        L = 0

        for R in range(len(nums)):
            
            # Shrink - uses L 
            if R - L > k:   # ----> Note the equation '>'  always visualize a small example
                hashset.remove(nums[L])
                L += 1
            
            # Check 
            if nums[R] in hashset:
                return True
            
            # Expand - uses R
            hashset.add(nums[R])
            

 
        return False
        '''


        ### HashSet and Sliding window ###
        # Check, Exapand and Shrink
        '''
        hashset = set() # Cur window of size <= k
        L = 0

        for R in range(len(nums)):
            
            # Check 
            if nums[R] in hashset:
                return True
            
            # Expand - uses R
            hashset.add(nums[R])
            
            # Shrink - uses L 
            if R - L >= k:     # ----> Note the equation '>='  always visualize a small example
                hashset.remove(nums[L])
                L += 1

        return False
        '''

            


        