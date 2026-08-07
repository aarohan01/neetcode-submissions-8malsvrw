class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        ### Bruteforce 
        '''
        maxprod = float('-inf')

        for i in range(len(nums)):
            curprod = 1
            for j in range(i,len(nums)):

                curprod *= nums[j]
                maxprod = max(maxprod,curprod)
        
        return maxprod
        '''

        ### Kadane's ###
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        prefix = suffix = 1

        for i in range(n):
            prefix = nums[i] * prefix if prefix != 0 else nums[i]
            suffix = nums[n - 1 - i] * suffix if suffix != 0 else nums[n-1-i]
            res = max(res, max(prefix, suffix))
        return res
                

