class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        ### If every number can be chose only once ###
        ### This gives correct - ex [2,5,6,9] target=7 ###
        '''
        res = []
        subset = []

        def dfs(index,csum):

            # Base case 1 - Failure
            if index >= len(nums) or csum > target:
                return 

            if csum == target:
                res.append(subset.copy())
                return 
            
            # Choice 1 - add the element 
            csum += nums[index]
            subset.append(nums[index])
            dfs(index+1,csum)

            # Choice 2 - not add the element
            csum -= nums[index]
            subset.pop()
            dfs(index+1,csum)

        dfs(0,0)
        return res
        '''


        #### NOT WORKING - Because wrong choices ###
        '''
        res = []
        subset = []
        
        def dfs(index,csum):

            # Base case 1 - Failure
            if index >= len(nums) or csum > target:
                return 

            # Base case 2 - Success
            if csum == target:
                res.append(subset.copy())
                return 
            

            # Choice 1 - add the element + advance the index\
            csum += nums[index]
            subset.append(nums[index])
            dfs(index+1,csum)


            # Choice 2 - not add the element + advance the index
            csum -= nums[index]
            subset.pop()
            dfs(index+1,csum)

            # Choice 3 - add the element + not advance the elemet
            csum += nums[index]
            subset.append(nums[index])
            dfs(index,csum)
            csum -= nums[index]
            subset.pop()

        dfs(0,0)
        return res
        '''


        ### Backtracking ###
        # Base case 1 is when index >= len or when sum more than target -> failure
        # Base case 2 when csum == target --> success
        # Always use success first then failure in backtracking
        # choice 1 -> keep taking the same number at index (repeating) thus not advancing index 
        # choice 2 -> not take and advance index
        # To take we need to add to subset and csum and to undo we need to pop and subtract
        # easy way is to pass csum + n  and csum added so we don't have to subtract it manually 
        # Possible third choice was to add and advance which, BUT This is already covered --
        # by take and stay --> take and stay will branch to take and stay or skip and advance thus also including the case
        # of take and advance.
        # If we again do explicit take and advance we will repeat these subsets.
        # Time: O(2^target/min(nums))  -> the longest branch is repeating characters but with min value so the leaf's at that level is max
        # since values higer will have even less branching terminating early.
        # Space: O(target / min(candidates)) aux -> at once this much is gonna be stored
        res = []
        subset = []
        
        def dfs(index,csum):

            # Base case 1 - Failure
            if index >= len(nums) or csum > target:
                return 
            
            # Base case 2 - Success
            if csum == target:
                res.append(subset.copy())
                return 

            
            # Better way to write is to pass the csum like index 
            """
            # Choice 1 - add the element + not advance index i.e keep adding current
            csum += nums[index]
            subset.append(nums[index])
            dfs(index,csum)
            csum -= nums[index]
            subset.pop()
        
            
            # Choice 2 - not add the element + advance the index i.e try another
            dfs(index+1,csum)
            """

        
            # Choice 1 - add the element + not advance index i.e keep adding current
            subset.append(nums[index])
            dfs(index,csum + nums[index])

            # Choice 2 - not add the element + advance the index i.e try another
            subset.pop()
            dfs(index+1,csum)
            

        dfs(0,0)
        return res
