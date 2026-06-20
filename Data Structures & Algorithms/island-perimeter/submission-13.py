class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:




        ### DFS normal multisource ###
        # Since only coverage once thus normal coverage
        # No source given, multisource
        # Either marking or visit set to use.
        # Need to mark as something else coz our return would be different if visisted
        # Idea : start from (0,0) and dfs till possible
        # The main idea is whenever failure base case is hit increment perimeter

        ## Recursion type - Return aggregation - similar to tree where we do left, right and combine return
        # Thus pemimeter is declared inside
        # Time : O(m*n)
        # space : O(m*n) -> Recursion stack
        '''
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r,c):

            ### Base Case - Failure ###
            # 1. min boundary
            # 2. max boundary 
            # 3. water - '0'


            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 1
            
            if grid[r][c] == -1:
                return 0

            
            ### Marking visit ###
            grid[r][c] = -1

            ### Subproblem ###
            perimeter = 0
            ## Recursion ###
            for dr, dc in directions:
                perimeter += dfs(r+dr,c+dc)

            ### Return to parent ###
            return perimeter

        
        ### Multisource to start from grid having value 1 ###

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r,c)
        '''

        ## Recursion type - Mutate state #### PREFER THIS OVER THE ABOVE ###
        # Thus pemimeter is declared outside
        # Time : O(m*n)
        # space : O(m*n) -> Recursion stack
        '''
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r,c):

            ### Base Case - Failure ###
            # 1. min boundary
            # 2. max boundary 
            # 3. water - '0'
            nonlocal perimeter

            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                perimeter += 1
                return
            
            if grid[r][c] == -1:
                return

            
            ### Marking visit ###
            grid[r][c] = -1

            ### Subproblem ###
            ## Recursion ###
            for dr, dc in directions:
                dfs(r+dr,c+dc)



        
        ### Multisource to start from grid having value 1 ###
        perimeter = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r,c)
        return perimeter
        ''' 

        ### Iteration - Optimal ###
        # NOT Iterative DFS , iteration #
        # Perimeter depends on the neighboring values
        # So instead of a DFS for each cell we can check the neighbors
        # If the neighbors are out of bounds or 0 count that border
        # Time: O(m*n)
        # Space: O(1)
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        perimeter = 0
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 1:

                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                            perimeter += 1
        return perimeter

                
        
