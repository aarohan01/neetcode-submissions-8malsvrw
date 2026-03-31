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
        '''
        nums.sort()
        res = set()


        # Loop and for every number find the pair that matches using two pointers
        for i in range(len(nums)):

            L = i + 1 
            R = len(nums) - 1

            while L < R:

                if nums[i] < -(nums[L]+nums[R]):
                    L += 1
                elif nums[i] > -(nums[L]+nums[R]):
                    R -= 1
                else:
                    res.add((nums[i],nums[L],nums[R]))
                    L += 1
                    R -= 1
        
        return [ list(i) for i in res ]
        '''

        ### Optimal : Sort + looped Two pointers, avoid duplicates during traversal ### 
        nums.sort()
        res = []


        # Loop and for every number find the pair that matches using two pointers
        for i in range(len(nums)):

            if nums[i] > 0:
                break 

            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            L = i + 1 
            R = len(nums) - 1

            while L < R:
                
                tsum = nums[i] + nums[L]+nums[R] 

                if tsum < 0:
                    L += 1
                elif tsum > 0:
                    R -= 1
                else:
                    res.append((nums[i],nums[L],nums[R]))
                    L += 1
                    R -= 1

                    while nums[L] == nums[L-1] and L < R:
                        L += 1
        
        return [ list(i) for i in res ]
