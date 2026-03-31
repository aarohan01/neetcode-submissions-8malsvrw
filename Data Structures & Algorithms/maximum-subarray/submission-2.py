class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ### Bruteforce ###
        # Given -> it will atleast have one element 
        # Loop and test all the combinations 
        # i tracks the start, j adds the sum starting i.
        # Time : O(n^2)
        # Space : O(1)
        '''
        ### dummy sum, set to first element since atleast one element ###
        maxSum = nums[0]

        # Loop 
        for i in range(len(nums)):
            curSum = 0
            for j in range(i,len(nums)):
                curSum += nums[j]
                maxSum = max(curSum, maxSum)
                print(f'c {curSum} m {maxSum}')
        return maxSum
        '''

        ### Kadane's Algo ###
        # Set maxSum to dummy/first element, xurSum as 0
        # What are we basically doing ? 
        # We are adding each element and keeping track of current sum
        # If the current sum is positive we are continuing with that subarray 
        # If the current sum becomes negative, we reset the curSum  to 0 and add the next element thus restarting 
        # the subarray from that element - Why ? coz adding negative sum to next element means the sum of that array will 
        # be lower than just having the next element 
        # Time : O(n)
        # Space : o(1)


        maxSum = nums[0]
        curSum = 0
        for n in nums:

            if curSum < 0:
                curSum = 0
            
            curSum += n
            maxSum = max(curSum, maxSum)
        
        return maxSum