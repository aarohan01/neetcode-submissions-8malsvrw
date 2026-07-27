class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        ### Bruteforce ###
        # Hashset + Sort and loop
        # Time : O(n^3)
        # Space : O(n)
        '''
        res = set()
        nums.sort()
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                for z in range(y+1,len(nums)):
                    if nums[x] + nums[y] + nums[z] == 0:
                        res.add((nums[x] , nums[y] , nums[z]))
        print(res)
        return [list(i) for i in res]
        '''

        ### Hashset + Sort + looped Two pointers ###
        # Time : O(n^2)
        # Space : O(n)
        '''
        nums.sort()
        res = set()


        # Loop and for every number find the pair that matches using two pointers
        for i in range(len(nums)):

            L = i + 1 
            R = len(nums) - 1

            while L < R:
                
                tsum = nums[i] + nums[L] + nums[R] 

                if tsum < 0:
                    L += 1
                elif tsum > 0:
                    R -= 1
                else:
                    res.append((nums[i],nums[L],nums[R]))
                    L += 1
                    R -= 1
        
        return [ list(i) for i in res ]
        '''

        ### Optimal : Sort + looped Two pointers, avoid duplicates of first and the the pair during traversal, skip positive first ### 
        # MUCH CLEANER MY VERSION AHEAD 
        # Time : O(n^2)
        # Space : O(1)
        '''
        nums.sort()
        res = []


        # Loop and for every number find the pair that matches using two pointers
        for i in range(len(nums)):
            
            # if i is positive all three will be positive thus not equal to 0
            if nums[i] > 0:
                break 

            # Avoid duplicate 1st numbers i.e i
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            # Two pointers
            L = i + 1 
            R = len(nums) - 1

            while L < R:
                
                tsum = nums[i] + nums[L] + nums[R] 

                # Move L or R according to required sum 
                if tsum < 0:
                    L += 1
                elif tsum > 0:
                    R -= 1
                else:
                    res.append((nums[i],nums[L],nums[R]))
                    L += 1
                    R -= 1


                    ### Avoid duplicates at the 2nd and 3rd point i.e L / R 
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
                    
                    ## OR 
                    
                    #while nums[R] == nums[R+1] and L < R:
                        #R -= 1
        
        return [ list(i) for i in res ]
        '''

        ### Sort + Two pointers + skip dupes at first pointer and 2nd pointer###
        # Sort 
        # One pointer to loop then -> Two pointers
        nums.sort()
        res = []
        for cur in range(len(nums)):

            # first once pointer, take and then skip any dupes
            if cur > 0 and nums[cur-1] == nums[cur]:
                continue

            L = cur+1
            R = len(nums)-1

            while L < R:
                
                # Take once and then skip any dupes 
                if L > cur + 1 and nums[L] == nums[L-1]:
                    L += 1
                    continue

                threesum = nums[cur] + nums[L] + nums[R]
                if threesum == 0:
                    res.append([nums[cur], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    # 2nd Pointer
                elif threesum < 0:
                    L += 1
                elif threesum > 0:
                    R -= 1
            

        return res



