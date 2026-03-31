class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ### Bruteforce ###
        minlen = float('inf')


        for L in range(len(nums)):
            cursum = 0
            for R in range(L,len(nums)):
                
                cursum += nums[R]

                if cursum >= target:
                    curlen = R-L+1
                    minlen = min(minlen,curlen)
                    break


        

        if minlen != float('inf'):
            return minlen
        return 0