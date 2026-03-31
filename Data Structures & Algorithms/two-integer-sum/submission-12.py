from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        ### Bruteforce ###
        # loop through and check 
        # Time : O(n^2)
        # Space : O(1)
        '''
        for i in range(len(nums)):
            for j in range(len(nums)):

                if i == j:
                    continue
                
                if nums[i] + nums[j] == target:
                    return [i,j]
        '''


        ### Solution 1 ###
        ## Use a hashmap. Loop through every number and check if difference between that and 
        # target exists in the hashmap or not. If it does not then add to the hashmapp else 
        # return 
        
        hashMap = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference not in hashMap:
                hashMap[nums[i]] = i
            else:
                return [hashMap[difference],i]



    
        