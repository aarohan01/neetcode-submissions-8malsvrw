class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ### Bruteforce ###

        maxSum = nums[0]

        for i in range(len(nums)):
            curSum = 0
            for j in range(i,len(nums)):
                curSum += nums[j]

                maxSum = max(curSum, maxSum)
        
        return maxSum

