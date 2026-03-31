class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        ### Solution 1 ### FAIL as it would still be n^2 to loop through it two times
        # Intuition : create a hashmap with all index value list  and sum as key 
        '''
        sum_dict = {}
        for i in range(len(nums)) :
        '''

        ### Solution 2 ### 
        ### Hint 1 ### Think of a mathematical equation ###
        ### Intuition : math eq can be :
        # Loop through the list and subtract the number from target and find that 
        # number in the list store both indices in a dictionary or other ds and return answer with smallest index
        '''
        result = []
        min_index  = len(nums) - 1
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums:
                #result.append([i,nums.index(remainder)])
                ### based on condition there won't be case of same index in combination with other i.e [0,2] [0,5]
                if min(i,nums.index(remainder)) < min_index :
                    result = [i,nums.index(remainder)]
                    min_index = min(i,nums.index(remainder))
        return result
        '''
        ### Solution 3 ### 
        # Use mathematical equation such that loop through -
        # the list and subtract from target and store the index and target index as -
        # key value in dictionary.
        '''
        result = {}
        for i in range(len(nums)):
             remainder = target - i
             result       
        '''

        ### Solution 4 ###
        # Build the dictonary of index and values first O(n)
        # Then use math equation to figure out O(n)
        # But unlike solution 3 this O(n) + O(n) or O(n) two times which is still O(n)
        ## DOESN't WORK 
        '''
        hash_map = {}
        for i in range(len(nums)):
            hash_map[i] = nums[i]
        print(hash_map)

        for i in hash_map:
        '''

        ### Solution 5 ###
        # After seeing the video : Two pointer but one pointer on array and another on hashmap
        # One pass using hashmap -
        # Empty hashmap for visited values of array value:index
        # We are visiting the array one by one and checking if its remainder exists in the hashmap
        # if it exists return the pair else add to the hashmap 
        # While returning hashmap stored index first because it will have lower index
        ###################
        ##### WORKS #######
        '''
        prevMap = {}
        for i in range(len(nums)):
            remainder =  target - nums[i] 
            if remainder in prevMap :
                return [prevMap[remainder],i]
            prevMap[nums[i]] = i            

        ### What to improve ###
        # Use enumerate everytime instead of using complicated way.
        # Solution below :
        '''
        prevMap = {}
        for i,n in enumerate(nums):
            difference = target - n
            if difference in prevMap:
                return [prevMap[difference],i]
            prevMap[n] = i