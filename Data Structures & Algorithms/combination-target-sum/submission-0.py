class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        ### If every number can be chose only once ###
        ### This gives correct - ex [2,5,6,9] target=7 ###
        '''
        res = []
        subset = []

        def dfs(index,csum):

            # Base case 1 - Failure
            if index >= len(nums):
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
        res = []
        subset = []
        
        def dfs(index,csum):

            # Base case 1 - Failure
            if index >= len(nums) or csum > target:
                return 

            if csum == target:
                res.append(subset.copy())
                return 
        
            # Choice 3 - add the element + not advance index i.e keep adding current
            csum += nums[index]
            subset.append(nums[index])
            dfs(index,csum)
            csum -= nums[index]
            subset.pop()
            
            
            # Choice 2 - not add the element + advance the index i.e try another
            dfs(index+1,csum)



        dfs(0,0)
        return res
