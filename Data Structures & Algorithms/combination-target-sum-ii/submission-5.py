class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        ### Backtracking - subset dupes type ###
        # No reuse so not reuse pattern 
        # Every to every thus subset pattern, dupes in input so subset dupes pattern
        # SINCE DUPES SORTING NECESSARY
        # Base case success -> sum == target 
        # Base case failure -> index >= len 
        # Choice 1 - Take and Adv
        # Choice 2 - Skip all occurences
        # Time: O(n*2^n)
        # Space: O(n) aux -> recursion stack


        ### IMP - SORTING ###
        candidates.sort()
        res = []
        subset = []

        def dfs(index,csum):
            
            # Base Case 1 - Success
            if csum == target:
                res.append(subset.copy())
                return 

            # Base Case 2 - Failure
            if index >= len(candidates) or csum > target:
                return 

            # Choice 1 - Take + advance
            subset.append(candidates[index])
            dfs(index+1,csum + candidates[index])

            # Choice 2 - Skip all occurence 
            # Undo first occurence
            subset.pop()
            while (index+1) < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            # Advance
            dfs(index+1,csum)
            #print(subset)

        dfs(0,0)
        return res