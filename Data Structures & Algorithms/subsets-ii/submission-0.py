class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # Sorting 
        nums.sort()


        # Backtracking
        res, subset = [], []
        def dfs(index):
            
            # Base Case -> Success
            if index >= len(nums):
                res.append(subset.copy())
                return 

            
            # Choice 1: Take and advance
            subset.append(nums[index])
            dfs(index + 1)

            # Choice 2: Skip all occurrence and advance
            # Pop the first occurence we appended
            subset.pop()
            while (index+1) < len(nums) and nums[index] == nums[index+1]:
                index += 1
            dfs(index + 1)

        dfs(0)
        return res

        