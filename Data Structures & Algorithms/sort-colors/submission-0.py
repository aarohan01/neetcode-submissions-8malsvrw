class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ### Solution ###
        # Since inplace can't be mergesort. 
        # Since constant space complexity cant be quicksort (logn) 
        # That leaves out insertion sort and bubble sort
        # Since we already know the input numbers which are limited to 0,1,2 bucket sort can be applied
        # Additionally time complexity is better on bubble sort

        # Frequency array 
        counts = [0, 0, 0]

        # Count the flags
        for i in nums:
            counts[i] += 1

        # Rewrite the original array 
        filled = 0

        for i in range(len(counts)):
            freq = counts[i]
            while freq != 0:
                nums[filled] = i
                freq -= 1
                filled += 1
        
