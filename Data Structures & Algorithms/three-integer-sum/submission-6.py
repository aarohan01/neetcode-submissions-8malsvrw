class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        ### Bruteforce ###
        res = set()
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                for z in range(y+1,len(nums)):
                    if nums[x] + nums[y] + nums[z] == 0:
                        res.add(tuple(sorted((nums[x] , nums[y] , nums[z]))))
        print(res)
        return [list(i) for i in res]
