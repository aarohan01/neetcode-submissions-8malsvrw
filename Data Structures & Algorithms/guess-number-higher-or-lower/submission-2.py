# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        

        ### Bruteforce ###
        # Just loop the range and ask 
        # Complexity : O(n)
        '''
        for i in range(1,n+1):
            if guess(i) == 0 :
                return i
        '''        


        ### Solution ###
        # Since range provided and we have to search, we can use binary range search
        # Complexity : O(logn)

        l = 1
        r = n

        while l <= r:
            m = (l+r)//2

            res =  guess(m)
            if guess(m) == -1 :
                r = m - 1
            elif guess(m) == 1 :
                l = m + 1
            elif guess(m) == 0 :
                return m
