class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ### Bruteforce ###
        maxp = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):

                maxp = max(maxp,prices[j]-prices[i])

            #maxp = max(maxp,curp)
        return maxp

        
        