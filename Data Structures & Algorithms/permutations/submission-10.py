class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res, permutation, visited = [], [], [False]*len(nums)

        def permute():

            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return

            for i in range(len(nums)):

                if not visited[i]:

                    permutation.append(nums[i])
                    visited[i] = True
                    permute()
                    

                    permutation.pop()
                    visited[i] = False

        permute()
        return res


