class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ### Bruteforce ###
        # Sort and return the k th element
        # Sort inplace + return 
        # Time : O(nlogn) + O(1) = O(nlogn)
        # Space : O(1)
        
        if nums and len(nums)>0:
            nums.sort()
            return nums[-k]
            
        return 