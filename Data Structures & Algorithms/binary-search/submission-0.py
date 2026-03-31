class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ### Solution ###
        # Sorted array + logn time complexity == Binary Search
        # Using two pointer system, only thing to keep in mind is even to stop if not element left 
        # thus l <= r not l < e
        l = 0
        r = len(nums)-1

        

        while l <= r:

            m = (l+r)//2
            
            if target < nums[m]:
                r = m-1
            elif target > nums[m]:
                l = m+1
            else :
                return m
        return -1