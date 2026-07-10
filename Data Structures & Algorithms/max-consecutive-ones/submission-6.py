class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:


        ### array counting ###
        # Take a pointer an count 1's and set max reset the counter if not 1 
        # Return max
        # Time: O(n)
        # Space: O(1)
        l = 0
        count = 0
        maxcount = 0

        while l < len(nums):
            if nums[l] == 1:
                count += 1
                maxcount = max(count, maxcount)
            else:
                count = 0

            l += 1

        return maxcount 
        