import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        ### Bruteforce ### 

        ### Two Pointers ## 
        # Issue :  First complex condition check again 
        # Issue :  Seprate check of empty instead of maintaining bounds within
        # Case 1 : Empty lists
        '''
        if not nums1 and not nums2:
            return 0
        # Case 2 : Empty list2
        elif not nums2:
            n = len(nums1)
            # Even
            if n % 2 == 0:
                return ((nums1[(n//2)-1] + nums1[(n//2)]) / 2)
            # Odd
            return nums1[(n//2)]
        # Case 2 : Empty list 1
        elif not nums1:
            n = len(nums2)
            # Even
            if n % 2 == 0:
                return ((nums2[(n//2)-1] + nums2[n//2]) / 2)
            # Odd
            return nums2[(n//2)]
        # Case 4 : Both not empty 
        else:
            tlen = len(nums1) + len(nums2)
            cur1, cur2 = 0, 0
            
            prevcurval = None
            curval = None
            curcount = 0

            while curcount <= tlen // 2:
                prevcurval = curval
                if cur1 < len(nums1) and (cur2 >= len(nums2) or nums1[cur1] < nums2[cur2]):
                    curval = nums1[cur1]
                    cur1 += 1
                else:
                    curval = nums2[cur2]
                    cur2 += 1
                curcount += 1

            # Odd 
            if tlen % 2 != 0:
                return curval
            else:
                return (prevcurval + curval)/2
        '''

        ### Bruteforce ###
        # prev, cur -> keep track of median need both if even else cur alone
        # count to track curlen or count
        # cur1 and cur2 pointers to track nums1 and nums2 

        # len is O(1) operation on arrays
        tlen = len(nums1) + len(nums2)

        count = 0
        cur1, cur2 = 0, 0
        prev, cur = None, None
        ## If even -> 8 elements -> median is cur 5 and prev 4 -> 8 // 2 + 1
        ## If odd -> 9 elements -> median is cur 5 -> 9 // 2  + 1
        while count < (tlen // 2) + 1:
            #print(f'{cur1}: val {nums1[cur1]} {cur2}: val {nums2[cur2]} c:{count}')
            prev = cur
            if (cur2 >= len(nums2)) or (cur1 < len(nums1) and nums1[cur1] <= nums2[cur2]):
                cur = nums1[cur1]
                cur1 += 1
            else:
                cur = nums2[cur2]
                cur2 += 1
            
            count += 1
        
        print(count)
        print(cur,prev)
        return cur if tlen % 2 != 0 else (cur+prev)/2
                

        


