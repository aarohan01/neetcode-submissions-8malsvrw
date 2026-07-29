
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       
      
      ### brute force ###
      # f(i) = min(cost[i]+f(i+1), cost[i]+f(i+2))
            dp =[None]*len(cost)
            def minCost(i):
       
                if i >= len(cost):
                    return 0
                if dp[i] is not None:
                    return dp[i]

                dp[i] = min(cost[i]+minCost(i+1), cost[i]+minCost(i+2))
                return dp[i]
            
            return min(minCost(0),minCost(1))
        