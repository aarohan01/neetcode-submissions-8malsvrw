
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       
        ### 
        # Costs function -> min cost to jump from i to n is cost[i] + min next 
        # State -> i 
        # Choices -> pay cost at i and then either jump 1 or 2 steps
        # Base cases when i reaches len(costs) 
        # return aggregation + combiner -> min(cost[i])
        '''
        def costs(i):
        
            if i >= len(cost):
                ### Cost from lens(nums) is 0 since its outside ###
                return 0
            
            mincost = cost[i] + min(costs(i+1),costs(i+2))

            return mincost
    
        return min(costs(0), costs(1))
        '''

        ### If we reverse direction the meaning changes to cost to reach i from i-1 and i-2
        # which will be cost[i-1] and memo 
        n = len(cost)
        memo = [None]*(n+1)
        ### If n == 0 i.e. len(cost) == 0  then 0 cost
        ## if n == 1 i.e. len(cost) is also 0 because we have choice between
        
        memo[0] = 0
        memo[1] = min(cost[0],memo[0])
        
        for i in range(2,n+1):
            memo[i] = min(cost[i-1] + memo[i-1], cost[i-2] + memo[i-2])
        
        return memo[n]
        
        ### brute force ###
        '''
          # f(i) = min(cost[i]+f(i+1), cost[i]+f(i+2))
          ## Aditionally at start two choices 
                n = len(cost)
                dp =[None]*(n+2)
                def minCost(i):
           
                    if i >= n:
                        return 0
                    if dp[i] is not None:
                        return dp[i]
        
                    dp[i] = min(cost[i]+minCost(i+1), cost[i]+minCost(i+2))
                    return dp[i]
                
                return min(minCost(0),minCost(1))
        '''
        
        
        ###### Bottom Up #####
        '''
        memo = [None]*(n+2)
        memo[0] = cost[0]
        memo[1] = min(cost[0],cost[1])
        
        if n <= 2:
            return 
        '''
        








        