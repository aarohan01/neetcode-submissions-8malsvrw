class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0
        hashset = set(nums)
        
        maxlen = 0
        for i in range(len(nums)):
            curlen = 0
            cur = nums[i]
            while cur in hashset:
                curlen += 1
                cur += 1
            maxlen = max(maxlen,curlen)

        print(maxlen)
        return maxlen
                