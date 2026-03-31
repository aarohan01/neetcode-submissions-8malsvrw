class Solution:
    def countBits(self, n: int) -> List[int]:

        ### Bruteforce ###
        def count(i):
            count = 0
            while i > 0:
                if i & 1 == 1:
                    count += 1
                i = i >> 1
            return count

            
        return [count(i) for i in range(n+1)]

        ### DP ###
        cache = [0]*(n+1)

        for i in range(n+1):
            
            # Calculate smaller values DP and by shifting and getting lower values bits
            cache[i] = cache[i>>1] + (i & 1)

            ## How this works
            # n = 5
            # i = 0
            # cache[0] = cache[0] + (0 & 1) = 0
            # cache[1] = cache[0] + (1 & 1) = 1
            # cache[2] = cache[1] + (1 & 1) = 2
            # and so on so its referring to old values 
            # Thus O(n+2) = O(n) calcualtions
        return cache
 