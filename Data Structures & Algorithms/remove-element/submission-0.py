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