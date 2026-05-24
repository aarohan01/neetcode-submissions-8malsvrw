class Solution:
    def findMin(self, nums: List[int]) -> int:


        ### Bruteforce ###
        #return min(nums)


        ### Binary Search ###
        # Modified binary search
        # If mid is greater than the rightmost value then the min is between mid and rightmost
        # Thus move the left beyond mid
        # If mid is lesser then answer could be mid or below
        # So we can record and move past like in this version OR in another version just move r to m instead of m-1
        # not needing recording
        '''
        l = 0
        r = len(nums)-1
        res = float('inf')
        while l <= r:

            m = (r+l)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                res = min(res,nums[m])
                r = m - 1
        return res
        '''
        ### Modified Binary Search - Other version ### 
        # use left as scanner, r as end
        # when l == r we have got result
        # can return either l or r but convention is return l
        
        l = 0
        r = len(nums)-1

        while l < r:

            m = (r+l)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 

        return nums[l]



            
        