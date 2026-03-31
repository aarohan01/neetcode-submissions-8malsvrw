class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ### Bruteforce ###
        # Main condition is sellday is after buyday 
        # For each buy day calculate max profit by calculating the diff
        # Time : O(n^2)
        # Space : O(1)
        '''
        maxp = 0
        for bd in range(len(prices)):
            for sd in range(bd+1,len(prices)):

                maxp = max(maxp,prices[sd]-prices[bd])

        return maxp
        '''


        ### Two Pointers ###
        L = 0
        R = len(prices)-1

        maxp = 0

        for R in range(1,len(prices)):

            diff = prices[R]-prices[L]
            

            maxp = max(maxp,diff)

            if diff <= 0:
                L = R
                
        return maxp
            



        
        