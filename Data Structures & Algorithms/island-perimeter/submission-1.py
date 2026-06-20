class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:




        ### DFS ###
        # Since only coverage once thus normal coverage
        # No source given, multisource
        # Either marking or visit set to use.
        # Need to mark as something else coz our return would be different if visisted
        # Idea : start from (0,0) and dfs till possible
        # The main idea is whenever failure base case is hit increment perimeter



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

        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res += dfs(r,c)
        
        return res

