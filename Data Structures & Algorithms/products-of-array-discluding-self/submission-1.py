class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:



        ### Bruteforce ###
        # Loop through nums and calculate the product 
        # Time : O(n^2)
        # Space : O(n)
        result = []

        for i in range(len(nums)):
            res = 1
            for j in range(len(nums)):
                if j != i:
                    res *= nums[j]
            
            result.append(res)
        
        print(result)
        return result
        


        ### Recursion ###
        

            
        