class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        ### Bruteforce ###
        '''
        
        L = 0

        while L < len(nums)-1:

            if nums[L] == 0 and L != len(nums)-1:
                return False

            for i in range(1,nums[L]+1):

           		if nums[L + nums[L]] != 0:
               		L += nums[L]
                    break
                
                    
            #if L >= len(nums):
                #return False
        return True
        '''
        dp = {} 
        def jump(idx):

            if idx in dp:
                return dp[idx]
             
            if idx >= len(nums)-1:
                return True
            if nums[idx] == 0:
                return False

            for i in range(nums[idx], 0, -1):
                if jump(idx+i):
                    dp[idx] = True
                    return True
            dp[idx] = False
            return False


        return True if jump(0) == True else False