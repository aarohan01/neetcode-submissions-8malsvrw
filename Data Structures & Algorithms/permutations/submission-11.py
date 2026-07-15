class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res, permutation, visited = [], [], 0

        def permute():
            nonlocal visited
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return

            for i in range(len(nums)):

                if visited & (1 << i) == 0:

                    permutation.append(nums[i])
                    visited |= (1 << i)
                    permute()
                    

                    permutation.pop()
                    visited &= ~(1 << i)

        permute()
        return res


