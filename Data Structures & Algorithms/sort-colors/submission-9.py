class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ### Solution ###
        # Counting Sort - The only problem is that this is 2 pass no 1.
        # Since inplace can't be mergesort. 
        # Since constant space complexity cant be quicksort (logn) 
        # That leaves out insertion sort and bubble sort
        # Since we already know the input numbers which are limited to 0,1,2 bucket sort can be applied
        # Additionally time complexity is better on bubble sort
        # Time : O(n)
        # Space : O(1)
        '''
        # Frequency table
        freq = [0]*3

        # Count the flags
        for i in nums:
            freq[i] += 1

        # Rewrite the original array 
        filled = 0

        for i in range(len(freq)):
            count = freq[i]
            while count != 0:
                nums[filled] = i
                count -= 1
                filled += 1
        '''
        
        ### Dutch national flag algorithm ###
        # L tracks 0, R tracks 2 and M tracks 1 as well as traverses
        # If M is 0 swap with L and move both forward
        # If M is 1 skip 
        # If M is 2 swap with R and only move R backward
        # Stop if M == R 
        # Time : O(n)
        # Space : O(1)
        
        if len(nums) <= 1:
            return 

        L, M, R = 0, 0, len(nums)-1

        while M <= R:
            if nums[M] == 0:
                nums[L], nums[M] = nums[M], nums[L]
                L += 1
                M += 1
            elif nums[M] == 1:
                M += 1
            elif nums[M] == 2:
                nums[R], nums[M] = nums[M], nums[R]
                R -= 1