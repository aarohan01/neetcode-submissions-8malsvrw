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
        # We need a grid same as size of m and n filled with None

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
        