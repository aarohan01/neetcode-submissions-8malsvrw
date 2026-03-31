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


        ### Division Allowed ###
        # Calculate the total product of the array and then divide it by each element, 
        # also will calculating product keep track of zeros
        # if one zero skip it and answer would be all zeros with skipped product at place of zero, 
        # if more than one zero answer would be all zeros.
        # Time : O(n)
        # Space : O(1)

        product = 1
        zcount = 0
        n = len(nums)
        output = [0]*n

        for i in range(n):

            if nums[i] == 0:
                zcount += 1
                
            
            if zcount > 1:
                return [0]*n
            else:
                if nums[i] != 0:
                    product *= nums[i]
                    print(product)
        
        
        for i in range(n):
            
            if zcount == 1:
                if nums[i] == 0:
                    output[i] = product
                    return output
            else:
                output[i] = product//nums[i]
        
        return output
                
                
            
            

        

        ### Prefix Suffix ###
        # Using normal prefix and suffix products 
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

        ### Prefix & SUffix shifted ###
        # For calculating product at i we need prefix[i-1] and Suffix[i+1], output[i] = prefix[i-1]*suffix[i+1]
        # But when i = 0 we don't need prefix and when i = n-1 we don't need suffix  (n=len)
        # At i=0, output[i] = 1 * suffix    (note suffix required here is 2nd not first)   
        # At i=n-1 output[i] = prefix * 1   (note prefix required here is 2nd last not last) 
        # So all we need for prefix is [1, from i=0 to n-1], suffix is [i=n-1 to 2,1] then our i's are aligned to output
        '''
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n

        for i in range(1,n):
            # Making use of prefix[i-1] since at i=1 prefix[i-1] we already set to 1
            prefix[i] = prefix[i-1] * nums[i-1]
        print(prefix)
        for i in range(n-2,-1,-1):
            # Making use of suffix[n-1] since at i=n-2 suffix[i-1] we already set to 1
            suffix[i] = suffix[i+1] * nums[i+1]
        print(suffix)
        output = [1]*n
        for i in range(n):
            # Since prefix values have shifted forward by 1 and suffix values shifted backward by 1
            output[i] = prefix[i]*suffix[i]
        
        return output
        '''

        #### Prefix + SUffix mem optimized ###
        # Better version below #
        '''
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
        '''
        

        ### Prefix & Suffix shifted mem optimized - Optimal ###
        # Instead of calculating prefix and suffixes before hand we do it on the fly in two passes
        # Store it in the output array directly 
        # Equation required for each i -> prefix * 1 * suffix
        # Leave the first and last as one only since output[0] = 1*suffix and output[n-1]=prefix*1
        # Pass One: Multiply by Prefix
        # Pass Two: Multiply by Suffix
        '''
        n = len(nums)
        pre, suff = 1,1
        output = [1]*n

        # First pass : prefix 
        # i = 0 needs to be 1 coz only suffix value
        for i in range(1,n):
            pre *= nums[i-1]
            output[i] = pre
        print(output)

        # Second pass : Suffix
        # i = n-1 needs to be 1 coz only prefix value
        for i in range(n-2,-1,-1):
            post *= nums[i+1]
            output[i] = post
        print(output)

        return output
        '''