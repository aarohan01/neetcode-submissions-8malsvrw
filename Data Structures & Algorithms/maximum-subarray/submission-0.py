class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ### Bruteforce ###
        # Given -> it will atleast have one element 
        # Loop and test all the combinations 
        # For every number 


        
        maxSum = nums[0]
        for i in range(len(nums)):
            curSum = 0
            for j in range(i,len(nums)):
                curSum += nums[j]
                maxSum = max(curSum, maxSum)
                print(f'c {curSum} m {maxSum}')
        return maxSum




