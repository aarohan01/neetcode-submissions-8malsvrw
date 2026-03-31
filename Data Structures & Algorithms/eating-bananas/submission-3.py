import math
class Solution:

    def condition(self, piles: List[int], k: int, h: int) -> bool :
        
        hours = 0
        for i in piles :
            hours += math.ceil(i/k)
            #print(f'k:{k} hours:{hours}')
        
        if hours > h:
            return True
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        ### Bruteforce ###
        # start with minimum number i.e 1 and keep checking if under h 
        '''
        k = 1
        hours = 0
        while True :
            for i in piles :
                hours += math.ceil(i/k)
                #print(f'k:{k} hours:{hours}')

            if hours <= h :
                return k
            else :
                k += 1
                hours = 0
        '''  


        ### Solution 1 ###
        # Intuition : Since we have to basically search for appropriate value of k 
        # we can make use of binary search to find it instead of going one by one


        l = 1
        r = max(piles)  # O(n)


        #hours = h+1

        # Binary search range 1..max(piles) for minimum number
        while l <= r :
            k = (l+r)//2
            con = self.condition(piles,k,h)
            if con:
                l = k + 1
            else :
                res = k
                r = k - 1
                
        return res





