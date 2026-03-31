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

        ### Sort + looped Two pointers avoid duplicates during traversal ###
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
 
