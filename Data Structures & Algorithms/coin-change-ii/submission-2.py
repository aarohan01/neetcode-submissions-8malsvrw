class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        ### State : amount
        # choices -> take and stay, adv for loop 
        # Base case when i reaches len(s)
        # return combo -> count 

        memo = {}
        def collect(i,rem):

            if rem == 0:
                return 1

            if i >= len(coins):
                return 0
            
            if (i,rem) in memo:
                return memo[(i,rem)]
            #count = 0
            
            skip = collect(i+1,rem)
            memo[(i,rem)] = skip
            if rem - coins[i] >= 0:
                take = collect(i, rem-coins[i])
                memo[(i,rem)] += take
                
                #count = take + skip
            

            
            return memo[(i,rem)]

        res = collect(0,amount)
        return res 