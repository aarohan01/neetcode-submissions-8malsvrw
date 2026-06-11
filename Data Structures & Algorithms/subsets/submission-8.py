class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        ### Backtracking ###
        # res, subset is global 
        # DFS on decision tree
        # Base case is when index reaches len -> store subset
        # Choice 1 - take and advance index 
        # Choice 2 - skip (undo) and advance index
        # Index is diff for each recursive call hence passing
        # Time: O(n * 2^n) -> approximate -> 2.2.2...ntimes (although more recursive calls but ignoring constants)
        # Space: O(n) aux 
        # Space : O(n*2^n) output -> 2^n sets with max n values, wrong in neetcode
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
        # Time: O(n*2^n)  -> res is worst case 2^n (approx) for every n  therefore n * 2^n (approx)
        # Space: O(2^n) or O(n*2^n)aux -> since we create copy of res everytime which is 2^n approx. (neetcode wrong given)
        # since its a copy hence reference i.e pointers not all elements but in some languages its n * 2^n , if res had 8 subsets then copy will have 8 pointers to those instead of n*8 elements and res is output array
        # Space : O(n*2^n) output -> 2^n sets with max n values, wrong in neetcode
    
        
        res = [[]]

        for n in nums:

            for r in res.copy():
                res.append( r + [n] ) 

        return res
        


        