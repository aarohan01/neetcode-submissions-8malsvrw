class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ### Bruteforce - Backtracking with set to avoid dupes ###
        # same pattern as subsets but handle dupes with set
        # use set for storing result and store it as tuple
        # No need to skip dupes
        # Time: O(n*2^n)
        # Space: O(n*2^n) aux -> set stores before returning list
        '''
        ### IMP - SORTING ###
        candidates.sort()
        res = set()
        subset = []

        def dfs(index,csum):
            
            # Base Case 1 - Success
            if csum == target:
                res.add(tuple(subset.copy()))
                return 

            # Base Case 2 - Failure
            if index >= len(candidates) or csum > target:
                return

            # Choice 1 - Take + advance
            subset.append(candidates[index])
            dfs(index+1,csum + candidates[index])

            # Choice 2 - Skip + Advance
            # Undo first occurence
            subset.pop()
            # Advance
            dfs(index+1,csum)
            #print(subset)

        dfs(0,0)
        return [list(i) for i in res]        
        '''

        ### Backtracking - subset dupes type ###
        # No reuse so not reuse pattern 
        # Every to every thus subset pattern, dupes in input so subset dupes pattern
        # SINCE DUPES SORTING NECESSARY
        # Base case success -> sum == target OR curtotal + curval > target or just curtotal > target
        # Base case failure -> index >= len 
        # Choice 1 - Take and Adv
        # Choice 2 - Skip all occurences
        # Time: O(n*2^n)
        # Space: O(n) aux -> recursion stack
        """
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
            '''
            if index >= len(candidates) or csum > target:
                return
            '''

            #'''More optimized base case 2 - failure : will stop even if possibility of csum going over target
            if index >= len(candidates) or csum + candidates[index] > target:
                return
            #'''


            # Choice 1 - Take + advance
            subset.append(candidates[index])
            dfs(index+1,csum + candidates[index])

            # Choice 2 - Skip all occurence 
            # Undo first occurence then skip other occurence
            subset.pop()
            while (index+1) < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            # Advance
            dfs(index+1,csum)
            #print(subset)

        dfs(0,0)
        return res
        """

        ### Backtracking Combination Style ###
        ## SORT + Skip all occurrences + take & stay + Undo ###

        candidates.sort()
        res = []
        subset = []

        def dfs(index,csum):
            
            # Base Case 1 - Success
            if csum == target:
                res.append(subset.copy())
                return
            


            for i in range(index,len(candidates)):

                if i > index and candidates[i] == candidates[i-1]:
                    continue

                if csum + candidates[i] > target:
                    break


                subset.append(candidates[i])
                dfs(i+1, csum + candidates[i])
                subset.pop()



        dfs(0,0)
        return res
