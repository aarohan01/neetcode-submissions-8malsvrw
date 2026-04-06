class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ### Bruteforce ###
        # Using Insertion sort or internal sorted method
        # But none of those are O(1)
        return nums.sort()
