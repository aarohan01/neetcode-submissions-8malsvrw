import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        ### Bruteforce ###
        # Merge and sort 
        # Time: O((m+n)log(m+n))
        # Space: O(m+n)
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[len(nums)//2] + nums[(len(nums)//2) - 1])/2
        return nums[(len(nums)//2)] 

        ### Bruteforce - Using Two Pointers ###
        # prev, cur -> keep track of median need both if even else cur alone
        # count to track curlen or count
        # cur1 and cur2 pointers to track nums1 and nums2 
        # prev and cur store median values
        # We move through both arrays using cur1 and cur2 and compare elements and update median till 
        # count of middle of total lenght is reached. Also need to take care of boundary case where 
        # a pointer is out of bounds in an array.
        # Time : O(m+n)
        # Space : O(1)
        '''
        # len is O(1) operation on arrays
        tlen = len(nums1) + len(nums2)

        count = 0
        cur1, cur2 = 0, 0
        prev, cur = None, None
        ## If even -> 8 elements -> median is cur 5 and prev 4 -> 8 // 2 + 1
        ## If odd -> 9 elements -> median is cur 5 -> 9 // 2  + 1
        while count < (tlen // 2) + 1:
        
            prev = cur

            # Boundary check - Either cur2 is passed boundary or (cur1 is within bounds and condition satisfied)
            # The boundary condition works because if cur2 >= len(nums2) it is guranteed than cur1 is inbounds
            # as median element is yet to reach i.e. nums1 has more elements and before reaching then end while 
            # loop will stop
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
        '''
                

        


