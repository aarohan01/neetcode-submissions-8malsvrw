class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        

        for num in nums:
            streak, curr = 0, num
            while curr in nums:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res