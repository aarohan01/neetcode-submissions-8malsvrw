class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:



        ### Bruteforce ###
        # Loop through nums and calculate the product 
        # Time : O(n^2)
        # Space : O(n)
        '''
        result = []

        for i in range(len(nums)):
            res = 1
            for j in range(len(nums)):
                if j != i:
                    res *= nums[j]
            
            result.append(res)
        
        print(result)
        return result
        '''


        ### Division ###
        # First find product of all array and then mutilply every number with that while dividing by itself
        # Time : O(n)
        # Space : O(1)
        '''
        mul = 1
        mulz = 1
        for n in nums:
            if n != 0:
                mul *= n
            if n == 0:
                mulz = 0
            
        print(mul)      

        output = []

        for n in nums:

            if mulz:
                if n == 0:
                    output.append(mul)
                else:
                    output.append(mulz)
            else:
                output.append(int(mul/n))

        return output
        '''
        

        ### Prefix Suffix shifted ###
        '''
        n = len(nums)
        prefix, suffix  = [1]*n, [1]*n
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i]
        
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i]

        print(prefix)
        print(suffix)

        output = [1]*n
        output[0] = suffix[1]
        output[-1] = prefix[-2]

        for i in range(1,n-1):
            output[i] = prefix[i-1] * suffix[i+1]
        
        return output
        '''



        #### Prefix + SUffix shifted ###

        n = len(nums)
        output = [1]*n

        pre = nums[0]
        for i in range(1,n):
            output[i] = pre 
            pre *= nums[i]
        print(output)

        suff = nums[-1]
        for i in range(n-2,-1,-1):
            output[i] *= suff
            suff *= nums[i]
        print(output)

        return output

        