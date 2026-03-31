class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        ### Bruteforce ###
        # Use two loops
        # Time: O(n^2)
        # Space: O(1)
        '''
        for i in range(len(nums)):
            for j in range(len(nums)):

                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
        '''

        ### Hashmap ###
        # if target - num is in hashmap return that index and current index
        # Time : o(n)
        # Space : O(n) -> In worst case store all elements

        HashMap = {}

        for i in range(len(nums)):
            
            res = target-nums[i]
            if res in HashMap:
                return [HashMap[res],i]
            else:
                HashMap[nums[i]] = i

    
        

        