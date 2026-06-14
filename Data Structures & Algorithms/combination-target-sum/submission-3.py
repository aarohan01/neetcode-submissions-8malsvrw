class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        ### If every number can be chose only once ###
        # Since reuse allowed this is Reuse backtracking pattern
        # Base case 1 - when sum == target -> Success
        # Base case 2 - index >= len or sum > target
        # Choice 1 - Take + Stay  : take + stay follwed by skip + adv == take + adv therefore no explicit 3rd choice
        # Choice 2 - Skip + Advance 
        ### This gives correct - ex [2,5,6,9] target=7 ###

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

