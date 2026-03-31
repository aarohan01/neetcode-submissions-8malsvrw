class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


        ### Bruteforce ###
        '''
        for i in range(len(nums)):

            if sum(nums[:i]) == sum(nums[i+1:]):
                return i

        return -1
        '''

        ### Prefix and Suffix sum shifted ###
        # Better versions below #
        '''
        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n

        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i-1]
        print(prefix)

        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] + nums[i+1]
        print(suffix)

        for i in range(n):

            if prefix[i] == suffix[i]:
                return i
        
        return -1
        '''

        ### Prefix only shifted ###

        '''
        n = len(nums)
        prefix = [0]*(n+1)
        res = []

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        print(prefix)

        for i in range(n):

            if prefix[i] == prefix[-1] - prefix[i+1]:
                return i
        
        return -1
        '''

        ### Prefix only mem optimized ###
        n = len(nums)

        total = 0

        for i in range(n):
            total += nums[i]
        print(f'Total prefix sum : {total}')

        prefix = 0
        for i in range(n):

            if prefix == total - nums[i]:
                return i
            else:
                total -= nums[i]
                prefix += nums[i]
        
        return -1


