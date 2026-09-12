class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        ### sort and check next ###
        # nlogn
        # 1
        '''
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False
        '''

        ### Hashset ###
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False