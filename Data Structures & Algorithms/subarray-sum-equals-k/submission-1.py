class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ### Bruteforce ###
        # For each element create a subarrays with sum k
        '''
        res = 0

        for i in range(len(nums)):
            cursum = 0
            for j in range(i,len(nums)):

                cursum += nums[j]
                if cursum == k:
                    res += 1
                    
        return res
        '''

        ### Prefixsum frequency hashmap + Prefixsum ###
        # The main problem with using prefix/shuffix is that inbetween arrays will be missed 
        # If we just used prefix/suffix to count these then it will be n^2 solution 
        # So to keep track of subarrays within current prefix that equal sum, we can subtract k from current prefix
        # This number is the prefix sum we are looking for in the hashmap
        # Q1. Why ? suppose [1,2,1] k = 3, current i=2 prefixsum is 3 so we know that if within this cursum prefix 
        # if any prefixsum equals cursum - k then we can remove that.
        # Q2. Why frequency and not just absent present ? 
        # Negative numbers ensure that prefixsums can be same within the arrays multiple times
        # Ex: [1, 2, -2, 0, 3] k=3  prefix sums -> [1, 3, 1, 1, 4] (for reference), Now notice that curprefix at i=4 is 
        # 4, and cursum(4) - k(3) == 1 which apprears 2 times in prefix sums that means there are two prefixsum arrays that total
        # to 1 they are [1] thus result [2, -2, 0, 3], [1,2,-2] resulting [0,3]
        # Now this is just one example as we traverse array to cover the case where the current prefix itself sums to k
        # We put a frequenct 0:1 so that cursum(3)-3 == 0 is also present in the freq hashmap 

        count = 0

        # Stores frequency of prefix sums encountered
        hashmap = {0:1}

        # Calculates current prefixsum
        cursum = 0
        for i in range(len(nums)):

            cursum += nums[i]

            prefixes = cursum-k
            count += hashmap.get(prefixes,0)
            hashmap[cursum] = hashmap.get(cursum,0) + 1
        
        return count



        