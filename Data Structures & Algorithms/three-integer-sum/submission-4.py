class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ### Solution after seeing solution ###
        # 3Sum =  sort + fix one digit + 2sum on others to satisfy condition 
        # In addition avoid duplicate on the fixed digit as well as 2sums so that the triplet is unique.
        # Why sort ? To use the 2sum 2 method to know when to move pointers.

        # Algo explanation :
        # 1st sort the array nlogn
        # Formula rewrite nums[i] + nums[j] = -nums[k] based on this we are gonna loop with 
        # a fixed point for loop and do two sum scan on other digits to check sum.
        # Now when we do we also check if sum > 0 or < 0 to move two pointers direction - 
        # since if sum of all three is > 0  that means we need lesser number for sum to be 0 hence decrease right pointer
        # or vice versa ( hence sorting previously required )
        # In case the sum is 0 then we can append results - Problem : this will be infinit loop 
        # as pointer won't move. In this case move from left to right all the time.
        # No to avoid duplicates : 1. the fixed point for loop skip if next number is same as previous
        # 2. In the two pointer since for every fixed pointer we are scanning the array from left to right, the chance for duplicate
        # is only on left, hence check for that ( This will ensure, duplicate avoidance on both sides), and skip left to next if dupe till less than r <-- IMP


        nums.sort()
        res = []


        #Fixing tht i pointer as first digit
        for i in range(len(nums)) :

            l = i + 1
            r = len(nums) - 1

            #skip if duplicate i to next, can happen only from 2nd digit --
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            while l < r :

                threeSum =  nums[i] + nums[l] + nums[r]
                print(threeSum)
                # Need lesser number in 2sum
                if  threeSum > 0:
                    r -= 1
                # Need bigger number in 2sum
                elif threeSum < 0:
                    l += 1
                # Add result and scan next number in the 2sum
                else :
                    print(f'T:y')
                    res.append([nums[i] , nums[l] , nums[r]])
                    l += 1     # scanning 

                    # Ensure next l isn't same ( r is not moving , we are scanning from l towards r)
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
        