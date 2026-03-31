class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:



        ### Solution 1 ###
        ## 1 is land and 0 is water and grid is surrounded by water.
        # Islands will be group of 1's surrounded by 0 or bounds.
        # For every node that is 1 we can perform DFS where moveing to 1's is allowed and 0's is not. 
        # Maintain a global visited list and not remove from it any node.
        # return after exploring neighbors. If able to return update a global counter that tracks number of islands
        # DFS Base Case  - 
        # 1. min(r,c) < 0  bound checking
        # 2. r/c == ROWS/COLS bound checking
        # 3. Node is 0 
        # 4. Node is already visited
        # Else add to visited global
        # Exlplore neighbors same way.



        count = 0
        visited = set()

        def dfs(grid, r, c, visisted):

            # Bounds            
            ROWS, COLS = len(grid), len(grid[0])

            # Base case to return 
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0" or (r,c) in visited:
                return 0
            
            res = 0
            visited.add((r,c))
            print(f'visiting {(r,c)}')

            res = dfs(grid, r+1, c, visited)
            res = dfs(grid, r-1, c, visited)
            res = dfs(grid, r, c+1, visited)
            res = dfs(grid, r, c-1, visited)

            return 1

        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                print(f'Starting at Row : {row} and Col : {col}' )
                res = dfs(grid, row, col, visited)
                if res == 1:
                    count += 1

        return count 





















        