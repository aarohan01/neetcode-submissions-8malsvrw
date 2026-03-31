class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ### Bruteforce ###
        # Main condition is sellday is after buyday 
        maxp = 0
        for bd in range(len(prices)):
            for sd in range(bd+1,len(prices)):

                maxp = max(maxp,prices[sd]-prices[bd])

        return maxp

        
        