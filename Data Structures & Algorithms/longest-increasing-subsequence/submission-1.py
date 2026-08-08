class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        # state : i 
        # base cases when i reaches len(nums)
        # choices at every i is next greater than i 
        # return agg is max
        n = len(nums)
        memo = {}
        def getlis(i):

            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            lis = 1
            for j in range(i+1,n):
                if nums[j]  > nums[i]:
                    lis = max(lis, 1+getlis(j))
            memo[i]= lis


            return memo[i]

        return max(getlis(i) for i in range(n))

