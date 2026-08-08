class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        ### State : amount
        # choices -> take and stay, adv for loop 
        # Base case when i reaches len(s)
        # return combo -> count 
        #coins.sort()
        memo = {}
        def collect(i,rem):

            if rem == 0:
                return 1

            if i >= len(coins):
                return 0
            
            if (i,rem) in memo:
                return memo[(i,rem)]
            
            count = collect(i+1,rem) 
            if rem - coins[i] >= 0:
                count += collect(i, rem-coins[i])            
            memo[(i,rem)] = count

            
            return memo[(i,rem)]

        res = collect(0,amount)
        return res 