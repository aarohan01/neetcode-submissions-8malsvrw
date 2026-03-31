class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:


        ### DFS recursive ###
        ## Normal DFS just less conditions to check and only two directions and some blocked nodes
        # Time : O(2^m+n) 
        # From every node two branch recursion but every run will only cover m+n node instead of the ususal m*n
        # due to restriction 
        # Space : O(m+n) -> recursive stack calls at a time
        '''
        r, c = 0, 0
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        
        def dfs(r, c, ROWS, COLS):

            # Base case 1: Failure
            if r == ROWS or c == COLS or obstacleGrid[r][c] == 1:
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
        r, c = 0, 0
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        # Note here COLS first m rows of col size n
        cache = [[None]*COLS for _ in range(ROWS)]
        print(cache)

        def dfs(r, c, ROWS, COLS, cache):

            # Base case 1: Failure
            if r == ROWS or c == COLS or obstacleGrid[r][c] == 1:
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
        

        ### Bottom Up ###
        ## Iterative + tabulation 
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
            print(type(curRow))
            # Base case : current row last col is 1 
            curRow[-1] = 1
        
            
            # This can also work and ideally should have been this since every currRows 
            # last value is actually prevRows last value, but we know that its always 1 so we hardcoded
            #if r == ROWS-1:
            #    curRow[-1] = 1
            #else:
            #    curRow[-1] = prevRow[-1]
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