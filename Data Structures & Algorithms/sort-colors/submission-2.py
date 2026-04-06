class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ### Bruteforce ###
        # Using Insertion sort or internal sorted method
        # But none of those are O(1)
        #return nums.sort()

        ### Counting sort ###
        # Time : O(n)
        # Space : O(1)
        
        # Freq table 
        freq = [0]*3
        
        for i in nums:
            freq[i] += 1
        print(f'Freq array :{freq}')

        j = 0
        for i in range(len(freq)):
            count = freq[i]
            while count != 0:
                nums[j] = i
                count -= 1
                j += 1
        return nums


