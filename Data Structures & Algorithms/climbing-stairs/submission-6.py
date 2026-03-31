class Solution:
    def climbStairs(self, n: int) -> int:
        


        ### Bruteforce ###
        # Recursion
        def climb(n):

            if n <= 2:
                return n
            
            return climb(n-1) + climb(n-2)


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

        ### Bottom-Up ###
        ## Using array and memory optimization ##
        def climb(n):

            # Edge case 
            if n <= 2:
                return n

            # Memoization : note index 0 is 1 and index 1 is 2
            cache = [1, 2]
    
            for i in range(3, n+1):
                
                # Rolling : Memory Optimization
                cache[0], cache[1] = cache[1], cache[0] + cache[1]
                
            
            return cache[1]
        
        return climb(n)
 
            


