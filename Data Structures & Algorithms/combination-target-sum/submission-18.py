class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        ### Backtracing subset reuse ###
        # Since reuse allowed this is Reuse backtracking pattern
        # Base case 1 - when sum == target -> Success
        # Base case 2 - index >= len or sum > target
        # Choice 1 - Take + Stay  : take + stay follwed by skip + adv == take + adv therefore no explicit 3rd choice
        # Choice 2 - Skip + Advance 
        ### This gives correct - ex [2,5,6,9] target=7 ###
        # Time: O(D * 2^(D+n)) where D -> target/min(nums) which is also max lenght of copy
        # but this is just shortened to D * 2^D  
        # For a n-ary tree the approx bound for calls is n^depth 
        # max depth here is gonna be D + n approx coz say target is 10 and min(num) is 2 then we can take 2 4 times then skip 
        # all n numbers which makes depth D - 1 + n 
        # Space: O(D)
        '''
        res = []
        subset = []

        def dfs(index,csum):
            
            # Base case 1 - Success
            if csum == target:
                res.append(subset.copy())
                return 

            # Base case 2 - Failure
            if index >= len(nums) or csum > target:
                return 
            
            # Choice 1 - Take + Stay 
            #csum += nums[index]
            subset.append(nums[index])
            dfs(index,csum + nums[index])

            # Choice 2 - Skip + Adv
            #csum -= nums[index]
            subset.pop()
            dfs(index+1,csum)

        dfs(0,0)
        return res
        '''


        ### Sorting + Backtracing subset reuse ###
        # If we just sort beforehand then we can skip all instances where sum and nums[index] /index+1 is going to be more
        # Modify or add another base case 
        # Same complexity asymptotically.
        '''
        nums.sort()
        res = []
        subset = []

        def dfs(index,csum):
            
            # Base case 1 - Success
            if csum == target:
                res.append(subset.copy())
                return 

            # Base case 2 - Failure
            # base case 1 ensures no success if csum is lower and adding nums[index] makes it higher so will index+1 (same or more as sorted)
            # If csum + nums[index] > target then csum  will become higher and trip csum > target next time if that was base case.
            if index >= len(nums) or csum + nums[index] > target:
                return 
            

            # Choice 1 - Take + Stay 
            #csum += nums[index]
            subset.append(nums[index])
            dfs(index,csum + nums[index])

            # Choice 2 - Skip + Adv
            #csum -= nums[index]
            subset.pop()
            dfs(index+1,csum)

        dfs(0,0)
        return res
        '''
        nums.sort()
        res = []
        subset = []
        def dfs(index, csum):
            
            if csum == target:
                res.append(subset.copy())
                return
            # Base Case : Failure
            if index >= len(nums):
                return 
            
            

            for i in range(index,len(nums)):
                
                if nums[i] + csum > target:
                    continue

                subset.append(nums[i])
                dfs(i, csum + nums[i])
                subset.pop()


        
        dfs(0,0)
        return res


                


        

