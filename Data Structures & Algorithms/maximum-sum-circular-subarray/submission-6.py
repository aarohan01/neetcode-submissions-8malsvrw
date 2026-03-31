class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:


        ### Bruteforce ###
        # Idea : for each number , calculate the curSum of subarrays and keep updating the max 
        # Since cannot be empty dummy value of maxSum be 0th element
        # First process the subrrays from each element i till the end, then continue with another loop to reach from 
        # 0 to i
        # Time : O(n^2)
        # Space : O(1)
        '''
        maxSum = nums[0]
        
        # Outer loop tracks the element, inner tracks the sub-array sums from that element
        for i in range(len(nums)):
            
            # For each subarray update this 
            curSum = 0

            # Process the elements after i 
            for j in range(i,len(nums)):

                curSum += nums[j]
                maxSum = max(curSum, maxSum)

            # Process the elements before i if contiguous after reaching  end in j loop
            for k in range(i):

                curSum += nums[k]
                maxSum = max(curSum, maxSum)
            
        return maxSum
        '''

        # Kadane 
        # Idea : it can be in between the array or part in front and back.
        # Part in between can be dealth with normal kadane global max, but if its other then 
        # the idea is in that case the part in middle will be global min 
        # So we calculate globalmax, globalmin, curmin, curmax and total at once 
        # Return either globalmax or total - globalmin 
        # There is one edge case : all negatives - if all negatives then 
        # the globalmax will be negative , because if there is any positive element in the array, its value i.e array sum
        # would have been globalmax, so whatever the value of globalmax is that is the least negative return that 

        # Global array sums, maxSum dummy value
        maxSum, minSum = nums[0], 0

        # Current array sums
        curMax, curMin = 0, 0

        # Total 
        total = 0

        for i in range(len(nums)):

            curMax, curMin  = max(0, curMax), min(0, curMin)
            curMax += nums[i]
            curMin += nums[i]

            maxSum, minSum = max(curMax, maxSum), min(curMin, minSum)

            total += nums[i]

        if maxSum < 0:
            return maxSum
        return max(maxSum, total - minSum)








        