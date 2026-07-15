class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        ######### Completely different ########
        # Constrained backtracking / constrained permutaion
        # based on open brackets , closed brackets 

        '''
        ### Subsets - dupes ###
        # SORT +   TAKE and ADV OR SKIP ALL OCCURENCE and ADV


        brackets = ['(',')']*n

        res, subset = [], []

        def dfs(i):
            print(subset)
            # Base Case 1 : Success
            if len(subset) == len(brackets):
                res.append(''.join(subset))
                return 

            # Base Case 2 : Failure
            if i >= len(brackets):
                return 

            # Choice 1 :  Include - Take and Advance
            subset.append(brackets[i])
            dfs(i+1)

            # Choice 2 : Exclude - Skip all occurrence and Adv
            subset.pop()
            while (i+1) < len(brackets) and brackets[i] == brackets[i+1]:
                i += 1
            dfs(i+1)

            

        dfs(0)
        return res
        '''

        ### Sorted Input ###
        '''
        brackets = ['(']*n + [')']*n

        res, perms = [], []
        used = [False]*len(brackets)


        def dfs():

            if len(brackets) == len(perms):
                res.append(''.join(perms))
                return 

            

            for i in range(len(brackets)):

                if not used[i]:
                    
                    ### Skip all dupes till the last one
                    if (i+1) < len(brackets) and brackets[i] == brackets[i+1] and not used[i+1]:
                        continue
                    
                    # Take
                    perms.append(brackets[i])
                    used[i] = True

                    # Advance
                    dfs()

                    # Undo 
                    used[i] = False
                    perms.pop()

        dfs()
        return res
        '''
        
        ### Bruteforce - recursion ###
        # This solution is simple
        # Start with an empty array and keep selecting either open or close bracket
        # if length of pattern hits n*2 do a check for validity and add to result if valid
        # Time: O(2^2n * 2n) -> nary tree here binary, max height is 2n, O(2n) for copying
        # Space: O(n^2) aux O(n^2) + O(n), n^2 is for holing all elements in during one path as each level
        # of recusion in a path will hold max 2n so a path will hold 1+2+...2n 
        # O(n) for recursion stack
        '''
        res = []
        def checker(patternN):
            count = 0

            for bracket in patternN:
                if bracket == '(':
                    count += 1
                else:
                    count -= 1

                if count < 0:
                    return False

            return count == 0


        def generate(pattern):

            if len(pattern) == n*2:
                if checker(pattern):
                    res.append(''.join(pattern))
                return

            
            generate(pattern + ['('])
            generate(pattern + [')'])


        generate([])
        return res
        '''

            

        ### Backtracking -- Combine the check and pattern  ###
        # Instead of seperate pattern array, a global pattern array can be used and popped
        # Similarly the check can happen implicitly 

        res, pattern = [], []
        def dfs(openN, closeN):

            if openN == closeN == n:
                res.append(''.join(pattern))
                return

            if openN < n:
                pattern.append("(")
                dfs(openN+1, closeN)
                pattern.pop()

            ### The most important condition is this ###
            ## if we do closeN < n, the backtracking will allow starting with ')'
            # At the root of backtracking tree openN and closeN is 0 so after executing openN loop 
            # closeN loop will be executed with OpenN, closeN as 0
            # Thus closeN should only execute when its lower than openN so that it atmost becomes equal
            if closeN < openN:
                pattern.append(")")
                dfs(openN, closeN+1)
                pattern.pop()

        dfs(0,0)
        return res

                







