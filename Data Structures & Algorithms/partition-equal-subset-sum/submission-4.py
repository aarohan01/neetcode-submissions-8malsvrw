class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        halfsum = sum(nums) // 2

        # state i 
        # pick number in array such that its halfsum
        memo = {}
        n = len(nums)
        def part(i,rem):


            if rem == 0:
                return True
            if i >= n:
                return False
            if (i,rem) in memo:
                return memo[(i,rem)]
            ## Take and advance or skip implicit loop
            for j in range(i,n):
                if rem-nums[j] >= 0:
                    if part(j+1,rem-nums[j]):

                        memo[(i,rem)] = True
                        return True
            memo[(i,rem)] = False
            return memo[(i,rem)]
        
        return part(0,halfsum)