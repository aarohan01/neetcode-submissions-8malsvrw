class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ### Bruteforce ###

        for idx,i in enumerate(range(m,len(nums1))):

            nums1[i] = nums2[idx]

        print(nums1)
        nums1.sort()

