class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ### Bruteforce ###
        maxp = 0
        for i in range(len(prices)):
            curp = 0
            for j in range(i+1,len(prices)):
            
                
                curp = max(curp,prices[j]-prices[i])

            maxp = max(maxp,curp)
        return maxp

        
        