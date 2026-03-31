### DFS Solution : My own version ###
## This version is perfect if changing values of grid is not allowed.
# If changing values of grid are allowed a little easier way is given in solution, instead of a set, just mark the 
# grid value as 0 that eliminated it from

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:



        ### Solution 1 ###
        ## 1 is land and 0 is water and grid is surrounded by water.
        # Islands will be group of 1's surrounded by 0 or bounds.
        # For every node that is 1 we can perform DFS where moveing to 1's is allowed and 0's is not. 
        # Maintain a global visited list and not remove from it any node.
        # return after exploring neighbors. If able to return update a global counter that tracks number of islands.
        # The base case returns 0 while a success case returns 1 which is backpropagated to parent. if the ultimate result is 1,
        # we completed one complete loop.

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

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # Only start if not already visited
                if grid[r][c] == "1":
                    print(f'Starting at Row : {r} and Col : {c}' )
                    res = dfs(grid, r, c, visited)
                    if res == 1:
                        count += 1
        return count 





















        