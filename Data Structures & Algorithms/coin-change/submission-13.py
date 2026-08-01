class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        ### Combosum - Reuse -> sort + for loop to adv -> take and stay, skip and adv 
        '''
        coins.sort()
        res = float('inf')

        def combo(index,count,cursum):
            nonlocal res
            ### Success ###
            if cursum == amount:
                #print(count)
                res =  min(res,count)
                return 

            
            for idx in range(index,len(coins)):

                if cursum + coins[idx] > amount:
                    break

                combo(idx,count+1,cursum+coins[idx])

        combo(0,0,0)
        return res if res != float('inf') else -1
        '''

        ### Recursion ###
        # State -> what is needed to know to finish amount/remaining amount 
        # Base case -> rem is 0 then success, rem is more tehen failure
        # choices -> all coins 
        # Combiner -> min count of coins
        #coins.sort(reverse=True)

        '''
        dp = {}
        def dfs(rem):

            if rem == 0:
                return 0

            if rem in dp:
                return dp[rem]

            # Default root count is float('inf')
            # then we check all the brancing minimum if anything resets the count 
            count = float('inf')
            for c in coins:
                if rem - c >= 0:
                    count = min(count,1 + dfs(rem - c))
            
            dp[rem] = count
            return dp[rem]
            #return count

        res = dfs(amount)
        return res if res != float('inf') else -1

        '''

        ### Converting to Bottom up ###
        # What we know -> when remaining is 0 i.e. base case count is 0 
        # and remaining can be between 0 to amount initially set to infinity 
        # Tabulate this : count = min(count,1 + dfs(rem - c))
        # Create all states array set base case to 0 and loop from 1 (since base case was 0) to the amount
        # and table[count] =  min(table[Count], 1 + table[Count-c])

        table = [float('inf')]*(amount+1)
        table[0] = 0

                     
        if amount == 0:
            return 0

        for rem in range(1,amount+1):
            for c in coins:
                if rem - c >= 0:
                    table[rem] = min(table[rem], 1+table[rem-c])
        
        return table[amount] if table[amount] != float('inf') else -1

