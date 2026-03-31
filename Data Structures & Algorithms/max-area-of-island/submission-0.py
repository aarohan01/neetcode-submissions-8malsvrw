class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ### Solution ###
        ## Combination of Number of Islands and classic matrix DFS
        # Loop through each node if the node is 1 and not visited previously while maintaining a global visited set
        # In the loop perform dfs that returns the count of 1's
        # keep a variable maxArea = 0 that is updated if the return count is greater than the variable in the loop 
        # No need for success base case as we do not need to reach end of bounds.



        visited = set()
        maxArea = 0

        def dfs(grid, r, c, visited, area):
            
            ROWS, COLS = len(grid), len(grid[0])
    
            # Base Case : Failure
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r,c) in visited:
                return 0

            # Maintain count 
            #count = 0
            area += 1

            # Visit the node
            visited.add((r,c))

            # Visit neighbors
            area += dfs(grid, r+1, c, visited, 0)
            area += dfs(grid, r-1, c, visited, 0)
            area += dfs(grid, r, c+1, visited, 0)
            area += dfs(grid, r, c-1, visited, 0)

            return area



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    print(f'Starting row: {r} and col: {c}')
                    area = dfs(grid, r, c, visited, 0)
                    print(area)
                    if area > maxArea:
                        maxArea = area
        
        return maxArea
        