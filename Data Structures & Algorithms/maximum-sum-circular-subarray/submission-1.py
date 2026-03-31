class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:


        ### Bruteforce ###
        # Idea : for each number , calculate the curSum of subarrays and keep updating the max 
        # Since cannot be empty dummy value of maxSum be 0th element


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




        