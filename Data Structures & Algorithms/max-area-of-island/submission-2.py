class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ### DFS - normal coverage multisource ###
        # Visiting all the nodes only once non-overlapping paths thus normal coverage
        # No source given, can be disconnected so multisource
        # Idea is to start from cell with '1' value.
        # Return if base case of failure
        # Mark or add to visit set if value 1
        # Do it to all neigbors with value 1
        # When mulisource loop increment number of islands
        # Time: O(m*n) -> every node visited once
        # Space: O(m*n) -> recursion stack and/or visit set if used

        ROWS, COLS = len(grid), len(grid[0])
        #visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
  
        
        def dfs(r,c):
            
            nonlocal area
            ### Base Case 1 : Failure ###
            # Lower bounds
            # Grid end  Upperbounds
            # Marked or visited i.e. '0'
            # Water i.e. '0'

            #if min(r,c) < 0  or (r,c) in visited  or r == ROWS or c == COLS or grid[r][c] == '0':
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 

            ### Subproblem ###
            #visited.add((r,c))
            grid[r][c] = 0
            area += 1

            for dr, dc in directions:
                dfs(r+dr,c+dc)

        
        ### Multisource ###
        maxarea = 0
        for r in range(ROWS):
            for c in range(COLS):

                #if grid[r][c] == 1 and (r,c) not in visited:
                if grid[r][c] == 1:
                    area = 0
                    dfs(r,c)
                    maxarea = max(area,maxarea)
                    
                    
        return maxarea

                   