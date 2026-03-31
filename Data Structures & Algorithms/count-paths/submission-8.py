class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ### DFS recursive ###
        ## Normal DFS just less conditions to check and only two directions
        # Time : O(2^m+n) 
        # From every node two branch recursion but every run will only cover m+n node instead of the ususal m*n
        # due to restriction 
        # Space : O(m+n) -> recursive stack calls at a time
        '''
        r, c = 0, 0
        ROWS, COLS = m, n
        
        def dfs(r, c, ROWS, COLS):

            # Base case 1: Failure
            if r == ROWS or c == COLS:
                return 0
            
            # Base case 2: Success
            if r == ROWS-1 and c == COLS-1:
                return 1

            # Subproblem 
            count = 0
            
            count += dfs(r+1, c, ROWS, COLS)
            count += dfs(r, c+1, ROWS, COLS)

            return count
        
        return dfs(r, c, ROWS, COLS)
        '''

        ### Top-Down ###
        ## Recursive + Memoization ##
        # We need a grid same as size of m and n filled with 0
        # We just cache the solution and provide it.
        # Time : O(m*n) -> Each node only calculated one time
        # Space : o(m*n) -> every nodes value stored -> NOTE: More than the normal recursive solution
        '''
        r, c = 0, 0
        ROWS, COLS = m, n

        # Note here COLS first m rows of col size n
        cache = [[None]*COLS for _ in range(ROWS)]
        print(cache)

        def dfs(r, c, ROWS, COLS, cache):

            # Base case 1: Failure
            if r == ROWS or c == COLS:
                return 0
            
            # Base case 2: Success
            if r == ROWS-1 and c == COLS-1:
                return 1

            # Return from cache
            if cache[r][c] is not None:
                return cache[r][c]

            # Subproblem 
            count = 0
            
            count += dfs(r+1, c, ROWS, COLS, cache)
            count += dfs(r, c+1, ROWS, COLS, cache)

            # Memoization
            cache[r][c] = count 
            print(f'{r},{c} - {cache[r][c]}')

            # The filling will start at cache[3][6] i.e final as the parent function is [0][0]
            # This will backpropagate till top
            return cache[r][c]
        

        return dfs(r, c, ROWS, COLS, cache)
        '''

        ### Bottom Up ###
        ## Iterative + tabulation 
        # Time : O(m*n)
        # Space : O(n) from O(2n) 
        '''
        r, c = 0, 0
        ROWS, COLS = m, n

        # Non-existent row below the matrix just to hold the base case 
        prevRow = [0]*COLS

        # Oppsite direction From (right bottom cell towards [0][0])
        # For all rows, do something to Columns of each Row
        # In this case merge/add the previous rows next element and current element and cache
        # Ex: cache[4][4] will be prevRow 
        for r in range(ROWS-1, -1, -1):

            # The first actual row for caching results
            curRow = [0]*COLS
            
            # Base case : current row last col is 1 
            curRow[-1] = 1

            
            # This can also work and ideally should have been this since every currRows 
            # last value is actually prevRows last value, but we know that its always 1 so we hardcoded
            #if r == ROWS-1:
                #curRow[-1] = 1
            #else:
                #curRow[-1] = prevRow[-1]
            #

            # Other columns of that row, suppose curRow[3][2] will be prev[2] + curRow[2+1]
            # next of current  and current column of prevrow
            for c in range(COLS-2, -1, -1):
                print(f'{r}-{c}')
                curRow[c] = prevRow[c] + curRow[c+1]
            
            print(curRow)
            prevRow = curRow

        # This will actually be cache[0][0]
        return curRow[c]
        '''


        ### Bottom-Up - Optimal ### 
        ## More optimized version using just one array 
        # Time : O(m*n)
        # Space : O(n) 
        
        ROWS, COLS = m, n
        
        # Tablulation of Row with an extra column 
        # Directly going to use this row to store results starting last row of grid
        #In the grid each elements answer is next column's value and previous rows value same column
        # We know that if there existed a row below grid the path values would all have been zero
        # Similarly all the column values of extra column would be 0
        cache = [0]*(COLS+1)

        # Base case : We updated the base case before hand and now all other will be updated
        cache[COLS-1] = 1

        # In the grid each elements answer is next column's value and previous rows value same column
        # Apart from base case all values are prev values 
        # Starting last row, which our cache is 
        for r in range(ROWS-1, -1, -1):
            # Last column
            for c in range(COLS-1, -1, -1):
                # Since we are assuming these are previous values
                # current value =  previous value same col + next col value
                cache[c] = cache[c] + cache[c+1]
        
        return cache[c]
        

        ### Bottom Up - Inplace ###
        ## Using the grid itself to store the path value
        # Not possible since grid not given it will all be auxiliary m*n space or atleast n space



