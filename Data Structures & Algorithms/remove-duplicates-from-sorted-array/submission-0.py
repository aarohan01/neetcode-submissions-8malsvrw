class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        ### Bruteforce Solution ###
        # Intuition - Key word is sorted in non descending i.e ascending and not to worry about elements after unique 
        # convert to set sort it and replace the lists k unique values 
        # return the len of the set

        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)




        ### Solution 1 ###
        # Intuition : Failed # After seeing solution :
        # Since we only need to worry about position in arrays till unique elements 
        # The remianing elements can be anything
        # First element is always going to be unique so skip that.
        # After that use two pointer, one to scan the array and one to maintain unique poistion end
        # Both start from 1 index
        # Check if scanner previous value is same as current if yes just move scanner
        # if no copy to unique location and move both once

        unique = 1

        for scanner in range(1,len(nums)):

            if nums[scanner] != nums[scanner-1]:
                nums[unique] = nums[scanner]
                unique += 1
            
        return unique