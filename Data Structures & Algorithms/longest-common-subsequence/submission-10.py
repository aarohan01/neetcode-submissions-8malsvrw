class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:


        ### BruteForce ###
        ## Recursion - Longest -> max count
        ## 3 cases 
        # 1.first letter same - subproblem both text excluding the first letter
        # 2. not same case one subproblem - all of 1st string and leaving 1st letter of 2nd string
        # 3. not same case two subproblem - all of 2nd string and leaving 1st letter of 1st string
        # Base cases - when should it end ? 
        # Since count returns 0 or 1 but max with cases
        # Passing indexs >> passing lists/strings
        # Recurrence relation :
        # F(i,j) = 1 + F(i+1, j+1)  OR max(F(i+1,j), F(i,j+1))
        '''
        # Indexes - go from 0 to len(text)-1 
        i, j = 0, 0
        
        def common(i,j):
            
            # Base case 
            if i == len(text1) or j == len(text2):
                return 0

            # Base case : success + subproblem
            if text1[i] == text2[j]:
                return 1 + common(i+1,j+1)
            else:
                return max(common(i+1,j), common(i,j+1))

        return common(i,j)
        '''

        ### Top-Down - Recursion + Memoization ###
        ## text1 rows of length text2  + extra column and row
        
        m,n = len(text1), len(text2)
        cache = [[-1]*(n+1) for i in range(m+1)]
        print(cache)
        ## By drawing the cases we get that -> diagonal when equal and
        # down and right when not
        
        # Indexes - go from 0 to len(text)-1 
        i, j = 0, 0
        
        def common(i,j):
            
            
            # Base case 
            if i == m or j == n:
                return 0

            # Memoization return 
            if cache[i][j] != -1:
                return cache[i][j]

            # Base case : success + subproblem
            if text1[i] == text2[j]:
                cache[i][j] = 1 + common(i+1,j+1)
            else:
                cache[i][j] = max(common(i+1,j), common(i,j+1))

            print(f'{i}-{j}')
            return cache[i][j]

        return common(i,j)
        

        ### Bottom-Up ###
        ## Iterative + tabulation ##
        #cache = [[0]*()]












            



        