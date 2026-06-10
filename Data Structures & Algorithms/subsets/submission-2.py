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
            '''
            ### Better/stanard way is to include first ###
            # Choice 1 - Not incude
            dfs(index + 1)

            # Choice 2 - Include
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()   ### Check decision tree if we don't pop the parent when executes choice 1 will have more elemets.
            '''

            # Choice 1: Include
            subset.append(nums[index])
            dfs(index+1)

            # Choice 2: Exclude
            subset.pop()
            dfs(index+1)

            
        dfs(0)
        return res




        