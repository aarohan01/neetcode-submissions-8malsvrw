class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        ### 
        """
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
    """
        ### Iterative - Just to know , from solution ###
        #Start: [[]]
        #Add 1 → [[], [1]]
        #Add 2 → [[], [1], [2], [1,2]]
        #Add 3 → [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

        res = [[]]

        for n in nums:

            for r in res.copy():
                res.append( r + [n] ) 

        return res


        