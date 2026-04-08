import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        ### Bruteforce ###
        # Merge and sort 
        # Time: O((m+n)log(m+n))
        # Space: O(m+n)
        '''
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[len(nums)//2] + nums[(len(nums)//2) - 1])/2
        return nums[(len(nums)//2)] 
        '''

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

        ### Binary Search and Partitioning ###
        # tlen is the total length and hlen is half that
        # So idea is we need two partitions such that either equal elements in both in case of even 
        # or half and one more in case of odd
        # We can achieve this by partitioning the smaller array using binary search into half (mid)
        # so remaining elements = hlen - mid 
        # so we need these from the bigger array so we check if starting these no of elements fit our req 
        # to form left side of the combined partition by comparing the ends of each againts start of other's 2nd partition 
        # and depeding on that we modify l,r in the binary search of smaller partition to include more elements or not 
        # Now the final answer is min(1st part bigger array last element, 2nd part smaller array first element)
        # If even then its max(1st parts of both ends) and min(2nd parts of both starts)
        
        # Total and Half length of final array 
        tlen = len(nums1) + len(nums2)
        hlen = tlen // 2

        ## Binary search mid on smaller array
        # Find smaller array 
        if len(nums1) < len(nums2):
            sarr, barr = nums1, nums2
        else:
            sarr, barr = nums2, nums1
            
        

        # Index based ---------------------
        L, R = 0, len(sarr)-1

        while True:
            
            # Suppose sarr = 3 elements and barr = 5 elements
            # tlen = 8, hlen = 4
            # L = 0, R = 2, M = 1 -> index
            # Count sarr = 0,1 i.e 2 element
            # Count barr = 4 - 2 = 2 element
            # Later converting the count to indexes 
            # sarr[1],barr[1] -> left partitions ends
            # sarr[2],barr[2] -> right partitions starts

            # Mid index of smaller array
            M = L + (R-L)//2

            # Easier calculation of elements of sarray to include
            slen = M + 1 

            # Larger array -> count in the bigger array to include
            blen = hlen - slen
            

            '''
            #### ISSUE HERE - Previously using sliced arrays
            # Using Slices - inefficient
            # Doesn't handle empty partitions -> coz of empty slices
            '''
        
            print(L,M,R)
            # Instead of partition slices use indices and get only the required elements
            # Required elements - Last elements of part1's and first element of part2's
            # Since we have to compare the values 
            # When we partition and if left partition has no values to make comparisons still valid we need 
            # smallest possible value even though no value exists thus -inf
            # Similarly if its on right side [2,3 | ] we want highest thus inf
            sleft = sarr[slen-1] if slen-1 >= 0 else float('-inf')   # left
            sright = sarr[slen] if slen < len(sarr) else float('inf') # right
            bleft = barr[blen-1] if blen-1 >= 0 else float('-inf') # left
            bright = barr[blen] if blen < len(barr) else float('inf') # right
            print(f'bleft {bleft} sleft {sleft} sright {sright}  bright {bright}') 
            
            
            ### Correct partition 
            # Partitions are correct if the bleft <= sright and sleft <= bright
            if bleft <= sright and sleft <= bright:

                # Even case
                if tlen % 2 == 0:
                    return (max(bleft,sleft) + min(bright,sright))/2
                else:
                    return min(bright,sright)
            
            elif bleft > sright:
                L = M + 1
            elif sleft > bright:
                R = M - 1
        
        ### Easier version of partitioning using counts instead of index ###
        # The only difference is that i is the count instead of index M.
        # Assuming that M is count of elements
        '''
        # Total and half length
        tlen = len(nums1) + len(nums2)
        hlen = tlen // 2

        # Always binary search on smaller array
        if len(nums1) < len(nums2):
            sarr, barr = nums1, nums2
        else:
            sarr, barr = nums2, nums1

        # i = number of elements taken from smaller array into left partition
        L, R = 0, len(sarr)

        while L <= R:
            i = L + (R - L) // 2
            j = hlen - i

            # Boundary values
            sleft  = sarr[i - 1] if i > 0 else float('-inf')
            sright = sarr[i] if i < len(sarr) else float('inf')
            bleft  = barr[j - 1] if j > 0 else float('-inf')
            bright = barr[j] if j < len(barr) else float('inf')

            # Correct partition
            if sleft <= bright and bleft <= sright:
                if tlen % 2 == 0:
                    return (max(sleft, bleft) + min(sright, bright)) / 2
                else:
                    return min(sright, bright)

            elif sleft > bright:
                R = i - 1
            else:
                L = i + 1
        '''