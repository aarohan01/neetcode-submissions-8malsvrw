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
        # The only problem is counting sort is not one pass
        # Time : O(n)
        # Space : O(1)
        '''
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
        '''

        ### Dutch national flag algorithm ###
        if len(nums) <= 1:
            return nums

        L, M, R = 0, 0, len(nums)-1

        while M <= R:
            if nums[M] == 0:
                nums[L], nums[M] = nums[M], nums[L]
                L += 1
                M += 1
            
            elif nums[M] == 1:
                M += 1
            
            elif nums[M] == 2:
                nums[R], nums[M] = nums[M], nums[R]
                R -= 1

