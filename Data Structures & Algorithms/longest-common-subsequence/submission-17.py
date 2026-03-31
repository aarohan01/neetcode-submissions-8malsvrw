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
        # F(i,j) = 1 + F(i+1, j+1) {if} OR  max(F(i+1,j), F(i,j+1)) {if}
        # Time : O(2^(m+n))
        # Space : O(m*n)

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
        # Time : O(m*n)
        # Space : O(m*n)
        '''
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
        '''
        

        ### Bottom-Up ###
        ## Iterative + tabulation ##
        # Time : O(m*n)
        # Space : O(m*n)
        '''
        m,n = len(text1), len(text2)
        cache = [[0]*(n+1) for i in range(m+1)]
        print(cache)

        ROWS, COLS = m, n
        print(ROWS)
        print(COLS)
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                
                print(f'{r}-{text1[r]} {c}-{text2[c]}')
                if text1[r] == text2[c]:
                    cache[r][c] = 1 + cache[r+1][c+1]
                else:
                    cache[r][c] = max(cache[r+1][c], cache[r][c+1])
        
        return cache[0][0]
        '''


        ### Bottom-Up ###
        ## Space Optimized - Using only 2 rows
        ## Prefer this over using just one row as when diagonal is used it can get confusing
        # Time : O(m*n)
        # Space : O(min(m,n))
        '''
        # smaller rows
        if len(text2) > len(text1):
            text1, text2 = text2, text1

        m,n = len(text1), len(text2)
        
        # Extra column
        prevRow = [0]*(n+1)
        print(prevRow)

        ROWS, COLS = m, n

        for r in range(ROWS-1, -1, -1):
            curRow = [0]*(n+1)
            for c in range(COLS-1, -1, -1):

                if text1[r] == text2[c]:
                    curRow[c] = 1 + prevRow[c+1]
                else:
                    curRow[c] = max(prevRow[c],curRow[c+1])

            prevRow = curRow
        
        return curRow[0]
        '''


        ### Bottom-Up Optimal ###
        # we don't have a grid to overwrite 
        # we will need the og diag value for next row starting with 0
        # we will also need to store down and right values of previous
        # Time : O(m*n)
        # Space : O(min(m,n))

        # smaller rows
        if len(text2) > len(text1):
            text1, text2 = text2, text1
    
        m,n = len(text1), len(text2)
        
        ROWS, COLS = m, n

        cache = [0]*(n+1) 
        for r in range(ROWS-1, -1, -1):
            # start diag value
            diag = 0
            for c in range(COLS-1, -1, -1):  
                temp = cache[c]
                if text1[r] == text2[c]:
                    cache[c] = 1 + diag
                else:
                    cache[c] = max(cache[c],cache[c+1])
                diag = temp

            
        
        return cache[0]












            



        