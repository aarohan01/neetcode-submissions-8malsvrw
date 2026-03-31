class Solution:
    def rob(self, nums: List[int]) -> int:

        ### Intuition ###
        # Recursion

        ### Bruteforce ###
        # Recursion 
        # Always start small + what choice we have to make from current position 
        # Example : [1,2,3,4]
        # Here we have to make a choice at start itself : Choose 1 or 2 ?
        # If I choose 1 I have to choose 3  if I choose 1,3 I can't choose 2 
        # so max(1+3 , 2)
        # Recurrence relation : 
        # 1. If looking backward - F(i) = max(nums[i] + F(i-2), F(i-1)) i = n-1..0 when n is number of element and index i goes from n-1 to 0
        # Base case will be when nums[i] reaches lowest, i.e here i=0 and 1 i.e 1st and 2nd step 
        # 2. If looking forward - F(i) = max(nums[i]+F(i+2), F(i+1))
        # Base case when nums[i] forward i.e when i=n i.e beyond index n-1 

        '''
        ## Forward 
        def robHelper(n):
            
            # Base case
            if n >= len(nums):
                return 0
            
            # Subproblem 
            return max(nums[n] + robHelper(n+2), robHelper(n+1))


        return robHelper(0)

        
        ## Backward
        def robHelper(n):
            
            # Base case  ----- Doubt : choices we made at the start 
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0],nums[1]) 
            
            # Subproblem 
            return max(nums[n] + robHelper(n-2), robHelper(n-1))


        return robHelper(len(nums)-1)
        '''

        ### Memoized DP ###
        ## Using the forward recursion ##
        '''
        amount = [None]*(len(nums))

        def robHelper(n):
            
            # Base case
            if n >= len(nums):
                return 0
            if amount[n]:
                return amount[n]

            # Subproblem 
            amount[n] = max(nums[n] + robHelper(n+2), robHelper(n+1))

            # Return last 
            return amount[n]

        return robHelper(0)
        '''

        ### Bottom Up with mem optimized ###
        # Need to use backward looking

        ##### NOTE : IMPORTANT : KEEP IN MIND THAT BOTTOM UP IS NEVER RECURSIVE ######
        #### SO FIRST REMOVE THAT FROM BRAIN AND THEN SOLVE ####

        # Edge case :
        if len(nums) == 0:
            return 
        elif len(nums) == 1:
            return nums[0]
            
        def robHelper(n):
            
            ### NOTE : No base cases here as no recursion.

            # cache stores 1st and 2nd result i.e if only nums[0] was present then 
            # nums[0] would have been answer if 0 and 1 were present max of them would 
            # have been answer
            cache = [nums[0], max(nums[0], nums[1])]

            # Subproblem 
            for i in range(2,n+1):
                ### Note the mistake -  using recursion 
                # cache[0], cache[1] = cache[1] , max(nums[i] + robHelper(i-2), robHelper(i-1))
                ### i starts from 2, suppose we want the index 2 thene i = 2 
                ## then what we do 
                print(i)
                cache[0], cache[1] = cache[1] , max(nums[i] + cache[0], cache[1])

            return cache[1]

        return robHelper(len(nums)-1)





            
            
