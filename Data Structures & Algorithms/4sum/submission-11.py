class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        '''
        res = set()
        nums.sort()
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                for c in range(b+1,len(nums)):
                    for d in range(c+1,len(nums)):
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            res.add((nums[a],nums[b],nums[c],nums[d]))

        return list(res)
        '''

        # Idea : 

        nums.sort()
        res = []
        for i in range(len(nums)):
            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue
    

            for j in range(i+1, len(nums)):
                
                if j-1 > i and nums[j] == nums[j-1]:
                    continue

                L = j+1 
                R = len(nums)-1

                while L < R :

                    if L-1 > j and nums[L] == nums[L-1]:
                        L += 1
                        continue

                    total = nums[i] + nums[j] + nums[L] + nums[R]
                    #print([i,j,L,R])
                    if total == target:
                        res.append([nums[i] , nums[j] , nums[L] , nums[R]])
                        L += 1
                        R -= 1
                    elif total > target:
                        R -=  1
                    else:
                        L += 1

        #print(res)
        return res


