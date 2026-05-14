class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        

        ### Bounded Bruteforce ###
        '''
        res = 0
        for i in range(len(nums)):
            product = 1
            for j in range(i,len(nums)):

                product *= nums[j]

                if product < k:
                    res += 1
                else:
                    break
        return res
        '''

        res = 0
        L = 0
        product = 1
        for R in range(len(nums)):

            product *= nums[R]

            while product >= k and L <= R:
                product /= nums[L]
                L += 1

            res += (R-L+1)

        return res
