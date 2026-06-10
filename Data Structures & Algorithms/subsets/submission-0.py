class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # Global shared
        res = []
        subset = []

        def dfs(index):

            if index >= len(nums):
                # Copying O(n) worst case
                res.append(subset.copy())
                return 
            
            # Choice 1 - Not incude
            dfs(index + 1)

            # Choice 2 - Include
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()

        dfs(0)
        return res




        