class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


        ### Bruteforce ###
        '''
        for i in range(len(nums)):

            if sum(nums[:i]) == sum(nums[i+1:]):
                return i

        return -1
        '''

        ### Prefix and suffix sums ###
        n = len(nums)

        if n == 1:
            return 0


        prefix =[]
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix.append(total)
        print(prefix) 


        suffix = [0]*n
        total = 0
        for i in range(len(nums)-1,-1,-1):
            total += nums[i]
            suffix[i] = total
        print(suffix) 


        for i in range(n):
            
            if (i == 0 and suffix[1] == 0) or (i == n-1 and prefix[n-2] == 0):
                return i
            
            elif i != 0 and i != n-1 :
                print(i)
                if prefix[i-1] == suffix[i+1]:
                    return i
        return -1