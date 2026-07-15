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
        
        res = []


        def checker(patternN):
            
            count = 0
            for i in patternN:
                if i == '(':
                    count +=1 
                else:
                    count -= 1

                if count < 0:
                    return False
            if count != 0:
                return False
            return True


        def generate(pattern):

            if len(pattern) == n*2:
                if checker(pattern):
                    res.append(''.join(pattern))
                return

            
            generate(pattern + ['('])
            generate(pattern + [')'])


        generate([])
        return res


            


                







