class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ### Bruteforce ###
        '''
        minlen = float('inf')


        for L in range(len(nums)):
            cursum = 0
            for R in range(L,len(nums)):
                
                cursum += nums[R]

                if cursum >= target:
                    curlen = R-L+1
                    minlen = min(minlen,curlen)
                    break   #If not break it will take even more time

        if minlen != float('inf'):
            return minlen
        return 0
        '''

        ### Sliding window ###
        L = 0
        minlen = float('inf')
        curSum = 0
        for R in range(len(nums)):
            
            curSum += nums[R]
            print(f'R : {R} - curSum - {curSum}')
            while curSum >= target:
                curlen = R-L+1
                minlen = min(minlen,curlen)
                curSum -= nums[L]
                L += 1
                
            
                #print(f'curlen : {curlen} minlen : {minlen} curSum : {curSum}')

        if minlen != float('inf'):
            return minlen
        return 0

