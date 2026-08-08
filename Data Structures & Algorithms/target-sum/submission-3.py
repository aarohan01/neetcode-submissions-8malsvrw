class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        ## Every index can be added or subbed
        # not combination or permutaion since all the ints are used 

        # state - i,total
        memo = {}
        def dfs(i, total):

            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in memo:
                return memo[(i,total)]
            plus = dfs(i + 1, total + nums[i])
            minus = dfs(i + 1, total - nums[i])

            memo[(i,total)] = plus + minus
            return memo[(i,total)]
        return dfs(0,0)