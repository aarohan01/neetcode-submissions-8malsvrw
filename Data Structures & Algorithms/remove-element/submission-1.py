class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        ### Bruteforce ###
        # Create a new list.
        # Loop through nums and add non val elemnts to this list
        # Copy all the elements from new list to nums till k 
        # Return lenght on the new list 
        # Time Complexity : O(n)
        # Space Complexity : O(n)

        new_nums = list()

        for element in nums:
            if element !=  val:
                new_nums.append(element)
        
        nums[:len(new_nums)] = new_nums
        return len(new_nums)


        ### Solution 1 ###
        # Intuition : We have to do it inplace that means space complexity need to be O(1)
        # We need to use two pointers one to scan the list for val and one to track position for non-val elements


        tracker = 0
        for scanner in range(len(nums)):
            if nums[scanner] != val:
                nums[tracker] = nums[scanner]
                tracker =+ 1
        
        return tracker+1
