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