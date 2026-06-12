class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        ### Bruteforce -  Backtracking + set ### 
        ## Not optimal ##
        # Just normal subset backtracking but result is a set instead of array, and store subset as tuple in it
        # The set will contain all the subsets thus using that aux space
        # Time: O(n * 2^n)
        # Space: O(n * 2^n) -> In res set -> 2^n subset and max n elements in each
        """
        # Global shared
        nums.sort()   ########## VERY IMPORTANT ###########
        res = set()
        subset = []

        def dfs(index):

            if index >= len(nums):
                # Copying O(n) worst case
                res.add(tuple(subset.copy()))
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
        return [list(i) for i in res]
        """

        ### Backtracking  (Optimal)###
        # Subsets with repetion 
        # Sorting is must to skip the repetitions
        # res, subset is global 
        # DFS on decision tree
        # Base case is when index reaches len -> store subset
        # Choice 1 - take and advance index 
        # Choice 2 - skip all occurence and advance index 
        # Index is diff for each recursive call hence passing
        # Time: O(n * 2^n) -> approximate -> 2.2.2...ntimes (although more recursive calls but ignoring constants)
        # Space: O(n) aux 
        # Space : O(n*2^n) output -> 2^n sets with max n values, wrong in neetcode
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
            # Take and Advance here will also include the take + not advance since choice one followed by choice 2
            # is exactly that, if we did explicit choice 3 i.e. choice 3 that will add repeat set.
            subset.append(nums[index])
            dfs(index + 1)

            # Choice 2: Skip all occurrence and advance
            # Pop the first occurence we appended
            subset.pop()
            # To skip all occurence we advance the index till index val is same i.e. skip then we advance once more
            # Thus completely skipping that value
            while (index+1) < len(nums) and nums[index] == nums[index+1]:
                index += 1
            dfs(index + 1)

        dfs(0)
        return res




        