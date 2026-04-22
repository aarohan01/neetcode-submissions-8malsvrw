class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ### Bruteforce ###
        # Merge to end of nums1 and then sort inplace
        # Time: O(NlogN)
        # Space: O(1)
        '''
        for idx,i in enumerate(range(m,len(nums1))):

            nums1[i] = nums2[idx]

        print(nums1)
        nums1.sort()
        '''

        ### Three pointers ###
        # If this wasn't inplace a temporary array of size m+n can be use and compared with two pointers
        # and merged
        # But this is inplace, key observation is space at the end, so we can start from end.
        # If we start from end the values to fill will be largest values first, if we run out of nums1 values fill the nums2.
        # L, R are for nums1 and X is for nums 2
        # Time: O(m+n)
        # Space: O(1)

        L, R, X = m-1, m+n-1, n-1
        print(nums1, nums2)
        while X >= 0 and L >= 0:
            
            print(L,R,X)
            if nums2[X] >= nums1[L]:
                nums1[R] = nums2[X]
                X -= 1
            else:
                nums1[R] = nums1[L]
                #nums1[L] = 0
                L -= 1
            R -= 1
            print(nums1, nums2)

        while X >= 0:
            nums1[X] = nums2[X]
            X -= 1


        ### Three Pointer - Improved ###
        # The more cleaner yet same optimization approach is to realize we just use the R pointer f
        '''
        L, R, X = m-1, m+n-1, n-1
        print(nums1, nums2)
        while X >= 0:
            
            print(L,R,X)
            if nums2[X] >= nums1[L]:
                nums1[R] = nums2[X]
                X -= 1
            else:
                nums1[R] = nums1[L]
                nums1[L] = 0
                L -= 1
            R -= 1
            print(nums1, nums2)

        '''



