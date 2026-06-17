class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:




        ### DFS - non-verlapping ###
        # Idea is to visit all the nodes once
        # Start from any node that is 1 and dfs add to global visit
        # Then repeat with any other '1' node that has not been visited

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]


        def dfs(r,c):

        
            ### Base Case : Failure ###
            # Lower bounds
            # Grid end  
            # In visited 
            # Water i.e. '0'

            if min(r,c) < 0  or (r,c) in visited  or r == ROWS or c == COLS or grid[r][c] == '0':
                return 


            visited.add((r,c))

            for dr, dc in directions:
                dfs(r+dr,c+dc)



        islands = 0
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)
        return islands

                   