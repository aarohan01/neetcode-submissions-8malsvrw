class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        ### Bruteforce ###
        # Using Hashset 
        # Time : O(n)
        # Space : O(n)
        '''
        hashset = set()

        for i in nums:

            if i in hashset:
                return i
            hashset.add(i)
        '''

        ### Fast and Slow +  Slow and Slow ###
        # 0 is dummy head, real head starts from nums[0]
        # Two ways to write
        # Time: O(n)
        # Space: O(1)
        '''
        curfast, curslow = nums[0], nums[0]
        while True:
            curfast = nums[nums[curfast]]
            curslow = nums[curslow]
            if curfast == curslow:
                break
        print(curfast)

        newslow = nums[0]
        while True:
            if curslow == newslow:
                return curslow
            curslow = nums[curslow]
            newslow = nums[newslow]
        '''

        # OR
        '''
        curfast, curslow = 0, 0
        while True:
            curfast = nums[nums[curfast]]
            curslow = nums[curslow]
            if curfast == curslow:
                break
        print(curfast)

        newslow = 0
        while True:
            curslow = nums[curslow]
            newslow = nums[newslow]
            if curslow == newslow:
                return curslow
        '''

        ### Using index to store visited ###
        # Every no. 1 to n has corresspoding index num - 1 ( same amount of number and index)
        # We use this to our advantage and for every number we mark the calculate index as -ve unless
        # its already negative in that case we are see that number the second time

        for n in nums:

            if nums[abs(n)-1] < 0:
                return abs(n)
            
            nums[abs(n)-1] = -nums[abs(n)-1]
            #print(nums)
        
            
  
        

        