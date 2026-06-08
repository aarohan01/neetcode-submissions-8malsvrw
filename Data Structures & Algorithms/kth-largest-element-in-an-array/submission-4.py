class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        ### Bruteforce ###
        nums.sort(reverse=True)
        return nums[k-1]
        