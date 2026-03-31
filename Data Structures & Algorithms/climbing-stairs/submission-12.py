class Solution:
    def climbStairs(self, n: int) -> int:
        


        ### Bruteforce ###

        # Forward Looking 
        # Choice either 1 or 2 at current i i.e i+1 or i+2
        # Subproblem :  
        # F(i) = F(i+1) + F(i+2) where i goes fro n -> I can choose 1 step or 2 steps from current 
        # Base cases: If I choose 
        '''
        def climb(i):

            if i > n:
                return 0
            if i == n:
                return 1

            return climb(i+1) + climb(i+2)

        return climb(0)
        '''

        # Recursion O(2^n)
        '''
        def climb(n):
            
            if n <=2:
                return n

            return climb(n-1) + climb(n-2)

        return climb(n)
        '''
        
        #### Top-Down with forward ####
        '''
        cache = [None]*n
        def climb(i):

            if i > n:
                return 0
            if i == n:
                return 1
            
            # Return intermediate result 
            if cache[i] is not None:
                print(i)
                return cache[i]

            cache[i] = climb(i+1) + climb(i+2)
            return cache[i]
        
        
        return climb(0)
        '''

        ### Intuition ###
        # We can draw a tree and see that it is a recursive tree
        # If we check manually we can see :
        # n =  1 : 1, n = 2 : 2, n = 3 : 3, n = 4 : 5
        # That means n ways = n-1 + n-2 ways which is fibonacci like 
        # So can be solved using DP

        ### Top-Down ###
        ### Array version -  can use dict which will be much easier ###
        '''
        # Prefilled array for memoization
        # cache[0] will never be used but array will still have it so n+1 index n len
        cache = [None]*(n+1)

        def climb(n, cache):
            
            # Base case
            if n <= 2:
                return n
            
            # Memoization
            if cache[n] != None:
                return cache[n]
            
            # Subproblem
            cache[n] = climb(n-1, cache) + climb(n-2, cache)

            return cache[n]
        
        return climb(n, cache)
        '''


        ### Normal Bottom-Up ###
        # Growing the array as we go but confusing
        if n <= 2:
            return n
        
        def climb(n):

            cache = [1,2]
            for i in range(2,n):
                print(i)
                cache.append(cache[i-1]+cache[i-2])
            return cache[n-1]

        return climb(n)
        
        '''
        cache = [None]*(n+1)
        def climb(n):

            if n <= 2:
                return n

            cache[1] = 1
            cache[2] = 2
            for i in range(3,n+1):
                print(i)
                cache[i] = cache[i-1]+cache[i-2]
            return cache[n]

        return climb(n)


        ### Bottom-Up ###
        ## Using array and memory optimization ##
        def climb(n):

            # Edge case 
            if n <= 2:
                return n

            # tabulation : note index 0 is 1 and index 1 is 2
            cache = [1, 2]
    
            for i in range(3, n+1):
                
                # Rolling : Memory Optimization
                cache[0], cache[1] = cache[1], cache[0] + cache[1]
                
            
            return cache[1]
        
        return climb(n)
        '''

 
            


