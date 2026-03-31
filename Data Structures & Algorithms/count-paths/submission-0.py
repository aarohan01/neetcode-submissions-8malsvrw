class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        r, c = 0, 0
        ROWS, COLS = m, n

        ### DFS recursive ###
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
        