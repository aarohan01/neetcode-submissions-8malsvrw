class Solution:
    def rob(self, nums: List[int]) -> int:




        ### Forward Recursion ###
        # i go from index 0 to n-1 when n is reached just return nums[n]
        '''
        n = len(nums)
        def robHelper(i):

            # Base case 
            # when i reaches end and beyond
            if i >= n:
                return 0

            return max(nums[i] + robHelper(i+2), robHelper(i+1))

        return robHelper(0)
        '''
        
        ### Backward Recursion ###
        # Note n here is index actually 10 element is at 9th
        # How I came up 
        # n goes from n to 0
        # n == 0 then max(nums[0] + robhelper(-2), robhelper(-1))
        '''
        def robHelper(n):

            # Base case 
            # If we draw recursive tree when we reach f(2) we need num[2] , f(1) and f(0) 
            # When we reach f(1) it just needs to send back nums[1] f(-1) and f(0) needs to be 0 
            # Thus when n = 1 functions return 0 so that nums[1] can be propagated


            ### IMPORTANT - Biggest confusion is regarding index n and house 1 
            # House 1 is index 0 thus f(0) exists

            if n < 0:
                return 0
            if n == 0:
                return nums[0]


            return max(nums[n] + robHelper(n-2), robHelper(n-1))
        
        n = len(nums)-1
        return robHelper(n) 
        '''

        ### Top-Down ###
        ## Forward 
        '''
        n = len(nums)

        cache = [None]*(n+1)
        def robHelper(i):

            # Base case 
            # when i reaches end and beyond
            if i >= n:
                return 0

            # Intermediate 
            if cache[i] is not None:
                return cache[i]

            cache[i] = max(nums[i] + robHelper(i+2), robHelper(i+1))
            
            return cache[i]

        
        return robHelper(0)
        '''
        ## Backward 
        '''
        n = len(nums)-1
        # To cause less confusion alinging index values to element value, will keep index 0 None
        cache = [None]*(n+1) 
        def robHelper(n):

            # Base case 
            # If we draw recursive tree when we reach f(2) we need num[2] , f(1) and f(0) 
            # When we reach f(1) it just needs to send back nums[1] f(-1) and f(0) needs to be 0 
            # Thus when n = 1 functions return 0 so that nums[1] can be propagated
            if n < 0:
                return 0
            if n == 0:
                return nums[0]
            
            if cache[n] is not None:
                return cache[n]

            cache[n] = max(nums[n] + robHelper(n-2), robHelper(n-1))
            
            return cache[n]
    
        return robHelper(n) 
        '''

        ### Bottom Up ###
        ## Iterative 
        ## Non-Optimized 
        '''
        n = len(nums)-1
        # We go form n to 0 index for n+1 items 
        
        # No house
        if n < 0:
            return 0
        # One house
        if n == 0:
            return nums[0]
        
        cache = [None]*(n+1)

        def robHelper(n):
            
    
            # If only one house 
            cache[0] = nums[0]
            # If two houses
            cache[1] = max(nums[0],nums[1])

            # Now if more that 2 houses 
            for i in range(2,n+1):
                # The previous result i.e f(0) is stored in cache[0]
                # f(1) is stored in cache[1]
                # So f(2) is max(nums[2] + f(0) , f(1))
                cache[i] = max(nums[i]+cache[i-2], cache[i-1])
            
            return cache[n]

        return robHelper(n)
        '''

        ## Optimized
        # No house
        n = len(nums)-1
        if n < 0:
            return 0
        # One house
        if n == 0:
            return nums[0]


        def robHelper(n):
            
            cache = [None, None]
            # If only one house 
            cache[0] = nums[0]
            # If two houses
            cache[1] = max(nums[0],nums[1])

            # Now if more that 2 houses 
            for i in range(2,n+1):
                # The previous result i.e f(0) is stored in cache[0]
                # f(1) is stored in cache[1]
                # So f(2) is max(nums[2] + f(0) , f(1))
                #cache[i] = max(nums[i]+cache[i-2], cache[i-1])
                cache[0], cache[1] =  cache[1], max(nums[i]+cache[0], cache[1])
            
            return cache[1]

        return robHelper(n)
        



        