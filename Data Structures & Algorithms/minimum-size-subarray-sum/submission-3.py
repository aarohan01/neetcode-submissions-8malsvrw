class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ### Bruteforce ###
        minlen = float('inf')


        for i in range(len(nums)):
            curlen, cursum = 0, 0
            for j in range(i,len(nums)):
                
                cursum += nums[j]
                curlen += 1

                if cursum >= target:
                    minlen = min(minlen,curlen)
                    break
            
            if minlen == 1:
                return minlen
        

        if minlen != float('inf'):
            return minlen
        return 0