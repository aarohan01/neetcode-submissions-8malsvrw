class Solution:
    def rob(self, nums: List[int]) -> int:
        

        ### 
        # State - i 
        # Start point from i to len(nums)-2 if i == 0 
        # if i == 1 then until len(nums)-1
        # So base case depends on that 
        # choices at each stage take and adv or skip
        # return 
        if len(nums) == 1:
            return nums[0]
        # Flag -> started from 0
        memo = {}
        def robber(i,flag):

            if flag and i >= len(nums)-1:
                return 0
            
            if not flag and i >= len(nums):
                return 0
            if (i,flag) in memo:
                return memo[(i,flag)]
            total =  max(nums[i]+robber(i+2,flag), robber(i+1,flag))
            memo[(i,flag)] = total
            return total 

        return max(robber(0,True),robber(1,False))