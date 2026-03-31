class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        


        ### HashSet and Sliding window ###
        '''
        # window -> stores k elements
        window = set()

        # Left tracker
        L = 0

        for R in range(len(nums)):
            
            # Search window else add to window 
            if nums[R] in window:
                return True
            window.add(nums[R])      

            # Remove extra elemnts from window
            if  R - L > k:
                window.remove(nums[L])
                L += 1


        return False
        '''

        window = set() # Cur window of size <= k
        L = 0

        for R in range(len(nums)):

            if nums[R] in window:
                return True
            window.add(nums[R])
            
            if R - L >= k:
                window.remove(nums[L])
                L += 1

        return False


            


        